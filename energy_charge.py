import requests



def check():
    reqDic = {"schoolCode": "10356", "areaId": "1902201604208035", "buildingCode": "9cf8b921", "floorCode": "1004", "roomCode": "0422"}
    url = "https://application.xiaofubao.com/app/electric/queryRoomSurplus.htm"


    json = requests.post(url, reqDic).json()
    amount = json['data']['amount']

    return amount

    
if __name__ == "__main__":

    print(check())