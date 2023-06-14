import file_manager
import parking_spot_manager

def start_process(path):
    strList = file_manager.read_file(path) # 파일의 경로를 매개변수로 받아 file_manager 모듈의 read_file 함수 호출하여 문자열 리스트 반환받음
    strList = parking_spot_manager.str_list_to_class_list(strList) # 위의 문자열 리스트를 이용하여 parking_spot_manager 모듈의 str_list_to_class_list 함수로 parking_spot 객체의 리스트로 반환 받음
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(strList) # print_spots 함수 호출 
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                strList = parking_spot_manager.filter_by_name(strList, keyword) # 입력 받은 keyword를 함수의 인수로 사용
            elif select == 2:
                keyword = input('type city:')
                strList = parking_spot_manager.filter_by_city(strList, keyword) # 입력 받은 keyword를 함수의 인수로 사용
            elif select == 3:
                keyword = input('type district:')
                strList = parking_spot_manager.filter_by_district(strList, keyword) # 입력 받은 keyword를 함수의 인수로 사용
            elif select == 4:
                keyword = input('type ptype:')
                strList = parking_spot_manager.filter_by_ptype(strList, keyword) # 입력 받은 keyword를 함수의 인수로 사용              
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                locations = (min_lat, max_lat, min_lon, max_lon)
                strList = parking_spot_manager.filter_by_location(strList, locations) # 입력 받은 locations를 함수의 인수로 사용
            else:
                print("invalid input")
        elif select == 3: 
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break # 반복 종료
        else:
            print("invalid input")