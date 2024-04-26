from flask import Flask, render_template, request
import NBAComm as nbacomm
app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')
  
  """
    This function handles the search route and returns the game log data for the specified player.
    Args:
        
    Returns:
        dict: A dictionary containing the game log data for the specified player.
    """
@app.route('/search', methods=['POST'])
def search():
  if request.method == 'POST':
    player_name = request.form['query']
    current_player = nbacomm.Player(player_name)
    #convert gamelog to json
    player_info = current_player.get_common_player_info()
    game_log = current_player.get_game_log_data_with_nothing()
    return render_template('player_stats.html', gameLog = game_log, playerInfo = player_info)
  return 'Search page'


  


if __name__ == '__main__':
   app.run(debug = True)

