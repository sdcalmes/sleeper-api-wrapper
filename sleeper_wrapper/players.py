from .base_api import BaseApi 

class Players(BaseApi):
	def __init__(self):
		pass

	def get_all_players(self):
		return self._call("https://api.sleeper.app/v1/players/nfl")


	def get_top_players_by_position(self, season, position, order_by, top):
		players = self._call("https://api.sleeper.app/stats/nfl/{}?season_type={}&position[]={}&order_by={}".format(season, 'regular', position, order_by))
		top_list = {}
		for player in players:
			if top == 0:
				return top_list
			else:
				p = self._call("https://api.sleeper.app/players/nfl/{}".format(player['player_id']))
				top_list[player['player_id']] = p
			top -= 1


	def get_trending_players(self,sport, add_drop, hours=24, limit=25 ):
		return self._call("https://api.sleeper.app/v1/players/{}/trending/{}?lookback_hours={}&limit={}".format(sport, add_drop, hours, limit))
