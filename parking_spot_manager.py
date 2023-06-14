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

def filter_by_name(spots, name): # name을 기준으로 데이터를 필터링하는 함수
    nameList = [i for i in spots if name in i.get('name')]
    return nameList 

def filter_by_city(spots, city): # city를 기준으로 데이터를 필터링하는 함수
    cityList = [i for i in spots if city in i.get('city')]
    return cityList

def filter_by_district(spots, district): # distrcit를 기준으로 데이터를 필터링하는 함수
    districtList = [i for i in spots if district in i.get('district')]
    return districtList

def filter_by_ptype(spots, ptype): # ptype을 기준으로 데이터를 필터링하는 함수
    ptypeList = [i for i in spots if ptype in i.get('ptype')]
    return ptypeList

def filter_by_location(spots, locations): # location을 기준으로 데이터를 필터링하는 함수
    locationList = [i for i in spots if locations[0] < i.get('latitude') and i.get('latitude') < locations[1] and locations[2] < i.get('longitude') and i.get('longitude') < locations[3]]
    return locationList # filter_by_location 함수는 정용희 학우님의 코드를 참고하였습니다. 

def sort_by_keyword(spots, keyword): # parking_spot 클래스 객체의 리스트[spots]와 정렬기준[keyword]을 매개변수로 받아 정렬 수행
    sortSpot = sorted(spots, key=lambda spot: spot.get(keyword)) # sorted 함수 사용하여 정렬
    return sortSpot

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