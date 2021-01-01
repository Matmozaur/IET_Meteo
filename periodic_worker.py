# import requests
# import schedule
# import time
#
# def get_crc():
#     url = 'https://danepubliczne.imgw.pl/api/data/synop/station/krakow'
#     r = requests.get(url).json()
#     print(r)
#
#
# if __name__ == "__main__":
#     get_crc()
#     schedule.every(1).hour.do(get_crc)
#     # schedule.every().hour.do(job)
#
#     while True:
#         schedule.run_pending()
