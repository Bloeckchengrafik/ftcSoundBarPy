import requests
import json

class WifiCtrl:
    def __init__(self, ip):
        self.__ip = ip
    def __post(self, endpoint, payload):
        url = "http://{host}/api/{endpoint}".format(host = self.__ip, endpoint = endpoint)

        headers = {'Content-Type': 'text/json'}
        payload = json.dumps(payload)

        return requests.request("post", url, headers=headers, data=payload).text

    def __get(self, endpoint, payload):
        url = "http://{host}/api/{endpoint}".format(host=self.__ip, endpoint=endpoint)

        headers = {'Content-Type': 'text/json'}
        payload = json.dumps(payload)

        return requests.request("get", url, headers=headers, data=payload).text

    def getTrack(self):
        request = json.loads(self.__get("track", {}))

        numberTracks = request['tracks']
        tracks = []
        for i in range(0, numberTracks):
            tracks.append((i + 1, request['track#' + str(i)]))

        activeTrack = request['active_track'] + 1
        state = request['state']

        return tracks, activeTrack, state

    def play(self, id):
        request = self.__post("track/play", {"track": id})
        return

    def playPrevious(self):
        self.__post("track/previous", {})
        return

    def playNext(self):
        self.__post("track/next", {})
        return

    def stopActive(self):
        self.__post("track/stop", {})
        return

    def pause(self):
        self.__post("track/pause", {})
        return

    def resume(self):
        self.__post("track/resume", {})
        return

    def setVolume(self, volume, relative = False):
        if relative:
            request = self.__post("volume", {"volume": volume})
        else:
            request = self.__post("volume", {"relvolume": volume})
        return

    def getVolume(self):
        return int(json.loads(self.__get("volume", {}))["volume"])
