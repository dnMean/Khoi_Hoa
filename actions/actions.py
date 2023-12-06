# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from datetime import datetime, timedelta

class ActionHandleStep2(Action):
    def name(self) :
        return "action_handle_step_2"
    def run(self,dispatcher,tracker,domain):
        # topic = tracker.get_slot("topic")
        topic = tracker.latest_message['text']
        print(topic)
        if topic == "Danh mục 3":
            dispatcher.utter_message(text="VUI LÒNG ĐĂNG KÝ TẠI QUẦY")
            return [SlotSet("topic","danhmuc3")]
        if topic == "Danh mục 2":

            buttons = [
                {
                    "type": "postback",
                    "title": "PHIẾU LÝ LỊCH TƯ PHÁP SỐ 1-KHÔNG GHI TIỀN ÁN TIỀN SỰ",
                    "payload":"PHIẾU LÝ LỊCH TƯ PHÁP SỐ 1"
                },
                {
                    "type": "postback",
                    "title": " PHIẾU LÝ LỊCH TƯ PHÁP SỐ 2-CHI TIẾT TIỀN ÁN TIỀN SỰ",
                    "payload":" PHIẾU LÝ LỊCH TƯ PHÁP SỐ 2"                    
                }
            ]
            dispatcher.utter_message(text="XIN VUI LÒNG NHẬP PHIẾU LÝ LỊCH TƯ PHÁP MÀ BẠN MUỐN NỘP",buttons=buttons)
            return [SlotSet("topic","danhmuc2")]
        if topic == "Danh mục 1":
            buttons = [
                {
                    "type": "postback",
                    "title": "A1,A2,A3",
                    "payload":"A1,A2,A3"
                },
                {
                    "type": "postback",
                    "title": "B1,B2,C,D,E",
                    "payload":"B1,B2,C,D,E"
                }
            ]
            dispatcher.utter_message(text="XIN VUI LÒNG NHẬP LOẠI GPLX CỦA BẠN",buttons=buttons)
            return [SlotSet("topic","danhmuc1")]    
        


class Actionhandlelicense(Action):
    def name(self):
        return "action_handle_license"
    def run(self,dispatcher,tracker,domain):
        license = tracker.latest_message['text']
        print(license)
        if ("A" not in license ):
            dispatcher.utter_message(text="BẠN ĐÃ CÓ GIẤY KHÁM SỨC KHỎE CÔNG CHỨNG?")  
            return [] 
        else:        
            text = f"\nGIẤY TỜ 1: ĐƠN XIN ĐỔI GIẤY PHÉP LÁI XE-THEO MẪU- BẠN CẦN IN MẪU ĐƠN=>BẤM CHỌN, MÁY IN RA \nGIẤY TỜ 2: BẢN SAO CĂN CƯỚC CÔNG DÂN \nGIẤY TỜ 3: BẢN SAO GIẤY PHÉP LÁI XE  \nGIẤY TỜ 4: BIÊN LAI CHUYỂN TIỀN DỊCH VỤ ĐỔI GPLX:135.000Đ VÀO TÀI KHOẢN XÁC ĐỊNH TRƯỚC,THEO MẪU/PHIẾU THU TIỀN MẶT TẠI QUẦY"
            dispatcher.utter_message(text=text)   
    
            return [FollowupAction("action_payout_date")]            

class ActionHandleAffirmDeny(Action):
    def name(self):
        return "action_handle_affirm_deny"
    
    def run(self,dispatcher,tracker,domain):
        intent = tracker.latest_message["intent"].get("name")
        topic = tracker.get_slot("topic")
        print(topic)
        if topic == "danhmuc1":
            if intent == "affirm":
                buttons = [
                    {
                        "type": "postback",
                        "title": "DANH MỤC 1: ĐỔI GIẤY PHÉP LÁI XE DO NGÀNH GIAO THÔNG VẬN TẢI CẤP",
                        "payload":"ĐỔI GIẤY PHÉP LÁI XE DO NGÀNH GIAO THÔNG VẬN TẢI CẤP"
                    },
                    {
                        "type": "postback",
                        "title": "DANH MỤC 2: MẤT GIẤY PHÉP LÁI XE",
                        "payload":"MẤT GIẤY PHÉP LÁI XE"
                    }
                ]
                dispatcher.utter_message(text="CHỌN LOẠI HỒ SƠ:",buttons=buttons)
            if  intent=="deny":
                dispatcher.utter_message(text="VUI LÒNG CHUẨN BỊ, GIẤY KSK HỢP LỆ ĐƯỢC CẤP BỚI TT CHĂM SÓC SỨC KHỎE CÁN BỘ 01 HAI BÀ TRƯNG, TP HUẾ")
        elif topic == "danhmuc2":
            if intent == "affirm":
                buttons = [
                    {
                        "type": "postback",
                        "title": "Trẻ em, người cao tuổi, người khuyết tật, người thuộc hộ nghèo, người cư trú tại các xã khó khăn, đồng bào dân tộc thiểu số ở các xã đặc biệt khó khăn – YÊU CẦU CUNG CẤP GIẤY TỜ CHỨNG MINH – MIỄN PHÍ",
                        "payload":"Trẻ em, người cao tuổi, người khuyết tật, người thuộc hộ nghèo, người cư trú tại các xã khó khăn, đồng bào dân tộc thiểu số ở các xã đặc biệt khó khăn – YÊU CẦU CUNG CẤP GIẤY TỜ CHỨNG MINH – MIỄN PHÍ"
                    },
                    {
                        "type": "postback",
                        "title": "Học sinh, sinh viên, người có công với cách mạng, thân nhân liệt sỹ- YÊU CẦU CUNG CẤP GIẤY TỜ CHỨNG MINH - TIẾN HÀNH THANH TOÁN QUÉT MÃ QR HOẶC IN PHIẾU THANH TOÁN CÓ MÃ SỐ ĐẾN QUẦY THANH TOÁN - mức phí áp dụng là 100.000 VNĐ/lần/người.",
                        "payload":"Học sinh, sinh viên, người có công với cách mạng, thân nhân liệt sỹ- YÊU CẦU CUNG CẤP GIẤY TỜ CHỨNG MINH - TIẾN HÀNH THANH TOÁN QUÉT MÃ QR HOẶC IN PHIẾU THANH TOÁN CÓ MÃ SỐ ĐẾN QUẦY THANH TOÁN - mức phí áp dụng là 100.000 VNĐ/lần/người."
                    }
                ]
                dispatcher.utter_message(text="CHỌN LOẠI MIỄN GIẢM:",buttons=buttons)
            if  intent=="deny":
                buttons = [
                    {
                        "type": "postback",
                        "title": "CÁ NHÂN",
                        "payload":"CÁ NHÂN"
                    },
                    {
                        "type": "postback",
                        "title": "ỦY QUYỀN",
                        "payload":"ỦY QUYỀN"
                    }
                ]
            dispatcher.utter_message(text="VUI LÒNG CHỌN ĐỐI TƯỢNG NỘP",buttons=buttons)
        return []
class ActionchooseChangelicense(Action):
    def name(self):
        return "action_choose_change_license"

    def run(self,dispatcher,tracker,domain):
        topic = tracker.latest_message['text']
        print(topic)
        if "ĐỔI GIẤY PHÉP LÁI XE DO NGÀNH GIAO THÔNG VẬN TẢI CẤP" == topic :
            text = f"\nGIẤY TỜ 1: ĐƠN XIN ĐỔI GIẤY PHÉP LÁI XE-THEO MẪU- BẠN CẦN IN MẪU ĐƠN=>BẤM CHỌN, MÁY IN RA \nGIẤY TỜ 2: BẢN SAO CĂN CƯỚC CÔNG DÂN \nGIẤY TỜ 3: BẢN SAO GIẤY PHÉP LÁI XE \nGIẤY TỜ 4: GIẤY KHÁM SỨC KHỎE \nGIẤY TỜ 5: BIÊN LAI CHUYỂN TIỀN DỊCH VỤ ĐỔI GPLX:135.000Đ VÀO TÀI KHOẢN XÁC ĐỊNH TRƯỚC,THEO MẪU/PHIẾU THU TIỀN MẶT TẠI QUẦY"
            dispatcher.utter_message(text=text)
        else:
            text = f"\nGIẤY TỜ 1: ĐƠN XIN ĐỔI GIẤY PHÉP LÁI XE-THEO MẪU- BẠN CẦN IN MẪU ĐƠN=>BẤM CHỌN, MÁY IN RA \nGIẤY TỜ 2: BẢN SAO CĂN CƯỚC CÔNG DÂN \nGIẤY TỜ 3: BẢN SAO GIẤY PHÉP LÁI XE (Không bắt buộc) \nGIẤY TỜ 4: GIẤY KHÁM SỨC KHỎE \nGIẤY TỜ 5: BIÊN LAI CHUYỂN TIỀN DỊCH VỤ ĐỔI GPLX:135.000Đ VÀO TÀI KHOẢN XÁC ĐỊNH TRƯỚC,THEO MẪU/PHIẾU THU TIỀN MẶT TẠI QUẦY "
            dispatcher.utter_message(text=text)
        return [FollowupAction("action_payout_date")]

#noi dung 2
class ActionChoosejudicial(Action):
    def name(self):
        return "action_choose_judicial"
    def run(self,dispatcher,tracker,domain):
        text = tracker.latest_message['text']
        print(text)
        if text == "PHIẾU LÝ LỊCH TƯ PHÁP SỐ 1" :
            utter_text = "VUI LÒNG CHỌN SỐ LƯỢNG PHIẾU LÝ LỊCH TƯ PHÁP CẦN XÁC NHẬN:"
            dispatcher.utter_message(text=utter_text)
            return [SlotSet("juridical","phaply1")]
        else : 
            buttons = [
                {
                    "type": "postback",
                    "title": "CÁ NHÂN",
                    "payload":"CÁ NHÂN"
                },
                {
                    "type": "postback",
                    "title": "ỦY QUYỀN",
                    "payload":"ỦY QUYỀN"
                }
            ]
            dispatcher.utter_message(text="VUI LÒNG CHỌN ĐỐI TƯỢNG NỘP",buttons=buttons)
            return [SlotSet("juridical","phaply2")]


class Actionchoosenumberjudicial(Action):
    def name(self):
        return "action_choose_number_of_judicial"
    def run(self,dispatcher,tracker,domain):
        number = tracker.get_slot("number_of_judicial")
        print(number)
        text = "MỨC PHÍ XÁC NHẬN LÀ 200.000đ/lần/người. TỪ PHIẾU 03 TRỞ ĐI THÌ MỨC PHÍ LÀ THÊM 5.000đ/phiếu.\nNẾU BẠN THUỘC ĐỐI TƯỢNG MIỄN GIẢM VUI LÒNG CHỌN: CÓ HOẶC KHÔNG"
        buttons = [
                {
                    "type": "postback",
                    "title": "Có",
                    "payload":"có"
                },
                {
                    "type": "postback",
                    "title": "Không",
                    "payload":"không"
                }
            ]
        dispatcher.utter_message(text=text,buttons=buttons)
        return []

class Actionchooserepresentative(Action):
    def name(self):
        return "action_choose_representative"
    def run(self,dispatcher,tracker,domain):
        representative = tracker.latest_message['text']
        juridical = tracker.get_slot("juridical")
        if juridical=="phaply1":
            if representative == "CÁ NHÂN":
                text = "\nGIẤY TỜ 1: Tờ khai yêu cầu cấp Phiếu lý lịch tư pháp theo mẫu quy định (Mẫu số 03/2013/TTLLTP) - BẠN CẦN IN MẪU ĐƠN=>BẤM CHỌN, MÁY IN RA\nGIẤY TỜ 2: Photo CCCD, CMND hoặc hộ chiếu của người được cấp Phiếu lý lịch tư pháp \nGIẤY TỜ 3: BIÊN NHẬN THANH TOÁN: BẠN THANH TOÁN QUA MÃ QR TỰ TẠO DỰA VÀO CÁC LỰA CHỌN CÓ HOẶC KHÔNG; NẾU CÓ, VUI LÒNG ĐIỀN MÃ BIÊN NHẬN THANH TOÁN/ HOẶC BÁO SỐ TIỀN VÀ XÁC NHẬN THANH TOÁN TẠI QUẦY KÈM BIÊN NHẬN BỎ VÀO HỒ SƠ"
            else:
                text = "\nGIẤY TỜ 1: Tờ khai yêu cầu cấp Phiếu lý lịch tư pháp theo mẫu quy định (Mẫu số 04/2013/TTLLTP) -BẠN CẦN IN MẪU ĐƠN=>BẤM CHỌN, MÁY IN RA\nIẤY TỜ 2: Photo CCCD, CMND hoặc hộ chiếu của người được cấp Phiếu lý lịch tư pháp \nGIẤY TỜ 3: Văn bản ủy quyền trong trường hợp ủy quyền cho người khác làm thủ tục (trường hợp người được ủy quyền là cha, mẹ, vợ, chồng, con của người ủy quyền thì không cần văn bản ủy quyền chỉ cần photo Giấy chứng nhận kết hôn, Giấy khai sinh hoặc Sổ hộ khẩu.). Văn bản ủy quyền phải được công chứng, chứng thực theo quy định của pháp luật Việt Nam. Photo CCCD người được ỦY QUYỀN.\nGIẤY TỜ 4: BIÊN NHẬN THANH TOÁN: BẠN THANH TOÁN QUA MÃ QR TỰ TẠO DỰA VÀO CÁC LỰA CHỌN CÓ HOẶC KHÔNG; NẾU CÓ, VUI LÒNG ĐIỀN MÃ BIÊN NHẬN THANH TOÁN/ HOẶC BÁO SỐ TIỀN VÀ XÁC NHẬN THANH TOÁN TẠI QUẦY KÈM BIÊN NHẬN BỎ VÀO HỒ SƠ"
            dispatcher.utter_message(text=text)
            return [FollowupAction("action_payout_date")]
        elif juridical == "phaply2":
            if representative == "ỦY QUYỀN":
                text = "LÝ LỊCH NÀY CHỈ UỶ UYỀN KHI BẠN LÀ CHA HOẶC MẸ CỦA NGƯỜI CHƯA THÀNH NIÊN YÊU CẦU CẤP PHIẾU LÝ LỊCH – CHỌN CHA HOẶC MẸ"
                buttons = [
                    {
                        "type": "postback",
                        "title": "CHA",
                        "payload":"CHA"
                    },
                    {
                        "type": "postback",
                        "title": "MẸ",
                        "payload":"MẸ"
                    }
                ]
                dispatcher.utter_message(text=text,buttons=buttons)
                return []
            elif representative == "CÁ NHÂN":
                text = "GIẤY TỜ 1: Tờ khai yêu cầu cấp Phiếu lý lịch tư pháp theo mẫu quy định (Mẫu số 03/2013/TTLLTP) -BẠN CẦN IN MẪU ĐƠN=>BẤM CHỌN, MÁY IN RA\nGIẤY TỜ 2: Photo CCCD, CMND hoặc hộ chiếu của người được cấp Phiếu lý lịch tư pháp \nGIẤY TỜ 3: BIÊN NHẬN THANH TOÁN: BẠN THANH TOÁN QUA MÃ QR TỰ TẠO DỰA VÀO CÁC LỰA CHỌN CÓ HOẶC KHÔNG; NẾU CÓ, VUI LÒNG ĐIỀN MÃ BIÊN NHẬN THANH TOÁN/ HOẶC BÁO SỐ TIỀN VÀ XÁC NHẬN THANH TOÁN TẠI QUẦY KÈM BIÊN NHẬN BỎ VÀO HỒ SƠ"
                dispatcher.utter_message(text=text)
                return [FollowupAction("action_payout_date")]
class ActionPayoutDate(Action):
    def name(self):
        return "action_payout_date"

    def run(self,dispatcher,tracker,domain):
        current_date = datetime.now()
        new_date = current_date + timedelta(days=10)
        formatted_date = new_date.strftime('%Y-%m-%d')
        dispatcher.utter_message(f"Ngày trả: {formatted_date}")
        return[FollowupAction("action_choose_payment")]
class ACtionchoosepayment(Action):
    def name(self):
        return "action_choose_payment"
    def run(self,dispatcher,tracker,domain):
        text = "Chọn hình thức chọn kết quả:"
        buttons = [
                {
                    "type": "postback",
                    "title": "TRỰC TIẾP",
                    "payload":"TRỰC TIẾP"
                },
                {
                    "type": "postback",
                    "title": "BƯU ĐIỆN",
                    "payload":"BƯU ĐIỆN"
                }
            ]
        dispatcher.utter_message(text=text,buttons=buttons)
        return []

class ActionHandlePayment(Action):
    def name(self):
        return "action_handle_payment"
    def run(self,dispatcher,tracker,domain):
        message = tracker.latest_message['text']
        if message == "TRỰC TIẾP":
            text = " NẾU CHỌN TRỰC TIẾP XUẤT BIÊN NHẬN KÈM SỐ HỒ SƠ ĐỂ NGƯỜI TAO TÁC CHỤP HÌNH HOẶC IN RA BIÊN NHẬN"
        if message == "BƯU ĐIỆN":
            text = " NẾU CHỌN QUA BƯU ĐIỆN XUẤT IN BIÊN NHẬN KÈM YÊU CẦU BỔ SUNG BIÊN LẠI NỘP TIỀN DỊCH VỤ NHẬN KẾT QUẢ TẠI NHÀ LÀ 30.000Đ THEO THÔNG TIN SỐ HỒ SƠ, LỆ PHÍ ĐÃ CHUYỂN KHOẢN CHO TÀI KHOẢN ĐƠN VỊ VẬN CHUYỂN"
        dispatcher.utter_message(text=text)
        return []

#phap ly 2

class ActionHandleParents(Action):
    def name(self):
        return "action_handle_parents"
    
    def run(self,dispatcher,tracker,domain):
        parent = tracker.latest_message['text']
        if parent == "CHA" or parent =="MẸ":
            text = "GIẤY TỜ 1: Tờ khai yêu cầu cấp Phiếu lý lịch tư pháp theo mẫu quy định (Mẫu số 04/2013/TTLLTP) -BẠN CẦN IN MẪU ĐƠN=>BẤM CHỌN, MÁY IN RA\nGIẤY TỜ 2: Photo CCCD, CMND hoặc hộ chiếu của người được cấp Phiếu lý lịch tư pháp \nGIẤY TỜ 3: phôto Giấy khai sinh hoặc Sổ hộ khẩu để chứng minh cha/mẹ\nGIẤY TỜ 4: BIÊN NHẬN THANH TOÁN: BẠN THANH TOÁN QUA MÃ QR TỰ TẠO DỰA VÀO CÁC LỰA CHỌN CÓ HOẶC KHÔNG; NẾU CÓ, VUI LÒNG ĐIỀN MÃ BIÊN NHẬN THANH TOÁN/ HOẶC BÁO SỐ TIỀN VÀ XÁC NHẬN THANH TOÁN TẠI QUẦY KÈM BIÊN NHẬN BỎ VÀO HỒ SƠ"
            dispatcher.utter_message(text=text)
            return [FollowupAction("action_payout_date")]
        return []