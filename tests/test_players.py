from sleeper_wrapper import Players

def test_get_trending_players(capsys):
	players = Players()
	added = players.get_trending_players("nfl","add", 1, 4)

	dropped = players.get_trending_players("nfl","drop")

	# with capsys.disabled():
	# 	print(added)
	# 	print(dropped)

def test_get_top_players():
	players = Players()
	top_list = players.get_top_players_by_position('2020', 'QB', 'pts_half_ppr', 12)
	assert isinstance(top_list, dict)
	assert len(top_list) == 12
