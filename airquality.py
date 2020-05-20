import rumps, json, requests
url = 'http://api.airvisual.com/v2/city?city=Los%20Angeles&state=California&country=USA&key=f0df05ba-bd43-4506-b3ad-5515bd92e3b8'

class AirQuality(rumps.App):
    def __init__(self):
        self.url = 'http://api.airvisual.com/v2/city?city=Los%20Angeles&state=California&country=USA&key=f0df05ba-bd43-4506-b3ad-5515bd92e3b8'
        self.data = requests.get(url=self.url).json()['data']
        self.cities = ['Los Angeles']
        self.selected_city = 'Los Angeles'
        self.selected_quality = '0'
        self.sub_menu = []
        self.cities_menu()

        super(AirQuality, self).__init__("Air Quality", title = self.selected_city +
        ': ' + self.selected_quality + ' AQI')
        self.menu = [("Cities", self.sub_menu), None, "About"]

    def cities_menu(self):
        for city in self.cities:
            item = rumps.MenuItem(city, callback = self.get_quality)
            item.state = 0
            self.sub_menu.append(item)

    def get_quality(self, sender):
        self.selected_city = sender.title
        self.selected_quality = self.data['current']['pollution']['aqius']
        print(self.selected_city, self.selected_quality)
        super(AirQuality, self).__init__("Air Quality", title =
        self.selected_city + ': ' + self.selected_quality + ' AQI')


    @rumps.clicked('About')
    def about(self, sender):
        rumps.alert("This is an air quality app created by Bo Stevens.")



if __name__ == "__main__":
    AirQuality().run()