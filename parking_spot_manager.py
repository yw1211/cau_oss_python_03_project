class parking_spot: # parking_spot 클래스 생성
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = { # 딕셔너리 객체 __item 필드 생성
            'name': name,
            'city': city,
            'district': district,
            'ptype': ptype,
            'longitude': longitude,
            'latitude': latitude
        }

    def __str__(self): 
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
    def get(self, keyword='name'): # get 메소드 생성하여 매개변수로 문자열 keyword 받고, 기본인수 'name'으로 지정
        return self.__item.get(keyword) # __item[keyword]값 반환

def str_list_to_class_list(str_list): # 문자열 리스트[str_list]를 매개 변수로 받아 parking_spot 클래스 객체의 리스트로 변환 후 반환
    classList = list()
    for i in str_list:
        parking = i.split(',')
        spot = parking_spot(parking[1], parking[2], parking[3], parking[4], float((parking[5])), float((parking[6])))
        classList.append(spot)
    return classList

def print_spots(spots): #parking_spot 클래스 객체의 리스트[spots]를 매개변수로 받아 리스트에 저장된 모든 객체의 값 출력
    print(f"---print elements({len(spots)})---") # spots의 원소 개수 출력 위해 len 함수 사용
    for i in spots:
        print(i)

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
# if __name__ == '__main__':
    # print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    #spots = filter_by_district(spots, '동작')
    #print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)