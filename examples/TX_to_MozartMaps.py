import sys
from pathlib import Path

# Add parent directory to path so we can import src
script_dir = Path(__file__).parent
root_dir = script_dir.parent
sys.path.insert(0, str(root_dir))
input_parent_dir = str("src/input_files/Mozart_12-1_WuuE02_ASAP")

from src.functions import *
from src.functions.warp_score import TXT_to_Maps

audio_file = str(root_dir / input_parent_dir / "KOLESO04M.wav")
ASAP_annotations = str(root_dir / input_parent_dir / "Mozart_PP.txt")
# svg_score = str(root_dir / input_parent_dir / "SW andras.svg")
# maps_file = str(root_dir / input_parent_dir / "andras.maps.json")
# beat_file = str(root_dir / input_parent_dir / "beat_example1.npz")

TXT_to_Maps(ASAP_annotations, output_file=str(root_dir / input_parent_dir / "Mozart_PP.maps.json"), print_output=True)