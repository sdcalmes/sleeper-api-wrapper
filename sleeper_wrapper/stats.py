from sleeper_wrapper.base_api import BaseApi


class Stats(BaseApi):
    def __init__(self):
        self._base_url = "https://api.sleeper.app/stats/{}".format("nfl")
        self._projections_base_url = "https://api.sleeper.app/projections/{}".format("nfl")
        self._full_stats = None

    def get_all_stats(self, season_type, season):
        return self._call("{}/{}?season_type={}".format(self._base_url, season, season_type))

    def get_week_stats(self, season_type, season, week):
        return self._call("{}/{}/{}?season_type={}".format(self._base_url, season, week, season_type))

    def get_all_projections(self, season_type, season):
        return self._call("{}/{}?season_type={}".format(self._projections_base_url, season, season_type))

    def get_week_projections(self, season_type, season, week):
        return self._call("{}/{}/{}?season_type={}".format(self._projections_base_url, season, week, season_type))

    def get_player_week_stats(self, stats, player_id):
        try:
            return next((item for item in stats if item["player_id"] == player_id), None)
        except:
            return None

    def get_player_week_projections(self, projections, player_id):
        try:
            return next((item for item in projections if item["player_id"] == player_id), None)
        except:
            return None

    def get_player_week_score(self, stats, player_id):
        # TODO: Need to cache stats by week, to avoid continuous api calls
        result_dict = {}
        try:
            player_stats = next((item for item in stats if item["player_id"] == player_id), None)
        except:
            return None

        if stats:
            try:
                result_dict["pts_ppr"] = player_stats["stats"]["pts_ppr"]
            except:
                result_dict["pts_ppr"] = None

            try:
                result_dict["pts_std"] = player_stats["stats"]["pts_std"]
            except:
                result_dict["pts_std"] = None

            try:
                result_dict["pts_half_ppr"] = player_stats["stats"]["pts_half_ppr"]
            except:
                result_dict["pts_half_ppr"] = None

        return result_dict
