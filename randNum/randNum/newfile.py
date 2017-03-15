import requests


def panda():
     for i in range(10):
        requests.get("http://127.0.0.1:8000/rnum/q=%d" % i) 
        
if __name__ =="__main__":
    panda()
