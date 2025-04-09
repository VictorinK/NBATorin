'''Create a Player class, the player class should about to get  the player info and the game log data. Thus the data return from the NBA_API is organizing and I can get and set the player based on the player name that was seearch up.'''

from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog, commonplayerinfo
import json
import numpy as np
import pandas as pd

class Player:
  def __init__(self, full_name):
      self.full_name = full_name
      self.player_info_data = players.find_players_by_full_name(full_name)
      self.player_id = self.player_info_data[0]['id']
    
  """
    This function returns the player info from the Commonplayerinfo endpoint from NBA_api.
    Args:

    Returns:
        dict: A dictionary containing the player info for the specified player.
  """
  def get_common_player_info(self):
    player_log = commonplayerinfo.CommonPlayerInfo(player_id=self.player_id).common_player_info.get_dict()
    result_dict = {}
    for i in range(len(player_log["headers"])):
      result_dict[player_log["headers"][i]] = player_log["data"][0][i]

    return result_dict


    """
      This function returns the game log data for the specified player.
      Args: gl_season = current/select game season 
            ngames = the number of games
            gl_paremeters = the Options to  which data choose to be display ex. PTS, AST, REB, etc.
            
      Returns:
          dict: A dictionary containing the game log data for the specified player.
      """
   
    """
    This function returns the game log data for the specified player.
    Args:  gl_paremeters = the OptionS to  which data choose to be display ex. PTS, AST, REB, etc.
    
    Returns:
       dict: A dictionary containing the game log data for the specified player.
    """
  def get_game_log_data_with_nothing(self,season):

      gamelog_from_player = playergamelog.PlayerGameLog(player_id=self.player_id,
        season=season)
      #collects dataframe (game_date,pts,matchup and etc) of all games into player_log variable
      player_log = gamelog_from_player.get_data_frames()[0]
      gl_result_dict = {}
      gl_report_options = ['GAME_DATE', 'MATCHUP', 'WL',"PTS","REB","AST","STL","BLK","FGM","FGA","OREB","DREB"] 
      np_result_arr  = np.array(player_log.loc[0:7, gl_report_options])
      #print(np_result_arr)
      for options in gl_report_options:
        gl_result_dict[options] = []
      for i in range(0, len(gl_report_options)):
        for j in range(0, len(np_result_arr)):
          gl_result_dict[gl_report_options[i]].append(np_result_arr[j][i])
      #print(gl_result_dict)
      return gl_result_dict 
    
      """
      This function returns the player info for a specified player.
      Args:  
    
      Returns:
          dict: A dictionary containing the common player info for the specified player.
      """
  def get_player_info_data(self):
    return self.player_info_data
    """
    This function returns the player ID for a specified player.
    Args:  

    Returns:
        str: A dictionary containing the ID  for the specified player.
    """
  def get_player_id(self):
    return self.player_id

