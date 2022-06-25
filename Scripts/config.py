from pathlib import Path


class Config:
  RANDOM_SEED = 27
  ROOT_PATH = Path("../")
  REPO = "https://github.com/RYees/AgriTech---USGS-LIDAR/"
  LOG_FILE = ROOT_PATH / "log/PythonLidara.log"
  DATA_PATH = ROOT_PATH / "Data/"
  ASSETS_PATH = ROOT_PATH / "assets/"
  LAZ_PATH = DATA_PATH / "laz"
  TIF_PATH = DATA_PATH / "tif"
  SHP_PATH = DATA_PATH / "shp"
  IMG_PATH = DATA_PATH / "img"
  USGS_3DEP_PUBLIC_DATA_PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
