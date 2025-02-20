from pkgutil import get_data

import kaggle
import pandas

kaggle.api.authenticate()

kaggle.api.dataset_download_files("bryanchungweather/nba-player-stats-dataset-for-the-2023-2024", path=".", unzip =True)

