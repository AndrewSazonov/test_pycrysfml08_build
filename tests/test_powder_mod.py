import os
import sys
import math
import numpy as np
from numpy.testing import assert_almost_equal

from pycrysfml08 import powder_mod


os.environ['FULLPROF'] = os.path.dirname(powder_mod.__file__)  # access to Src/Databases/magnetic_data.txt

STUDY_DICT = {
  "phases": [
    {
      "SrTiO3": {
        "_space_group_name_H-M_alt": "P m -3 m",
        "_cell_length_a": 3.9,
        "_cell_length_b": 3.9,
        "_cell_length_c": 3.9,
        "_cell_angle_alpha": 90,
        "_cell_angle_beta": 90,
        "_cell_angle_gamma": 90,
        "_atom_site": [
          {
            "_label": "Sr",
            "_type_symbol": "Sr",
            "_fract_x": 0.5,
            "_fract_y": 0.5,
            "_fract_z": 0.5,
            "_occupancy": 1,
            "_adp_type": "Biso",
            "_B_iso_or_equiv": 0.40
          },
          {
            "_label": "Ti",
            "_type_symbol": "Ti",
            "_fract_x": 0,
            "_fract_y": 0,
            "_fract_z": 0,
            "_occupancy": 1,
            "_adp_type": "Biso",
            "_B_iso_or_equiv": 0.50
          },
          {
            "_label": "O",
            "_type_symbol": "O",
            "_fract_x": 0.5,
            "_fract_y": 0,
            "_fract_z": 0,
            "_occupancy": 1,
            "_adp_type": "Biso",
            "_B_iso_or_equiv": 0.65
          }
        ]
      }
    }
  ],
  "experiments": [
    {
      "NPD": {
        "_diffrn_source": "nuclear reactor",
        "_diffrn_radiation_probe": "neutron",
        "_diffrn_radiation_wavelength": 1.27,
        "_pd_instr_resolution_u": 0.02,
        "_pd_instr_resolution_v": -0.02,
        "_pd_instr_resolution_w": 0.12,
        "_pd_instr_resolution_x": 0.0015,
        "_pd_instr_resolution_y": 0,
        "_pd_instr_reflex_asymmetry_p1": 0,
        "_pd_instr_reflex_asymmetry_p2": 0,
        "_pd_instr_reflex_asymmetry_p3": 0,
        "_pd_instr_reflex_asymmetry_p4": 0,
        "_pd_meas_2theta_offset": 0,
        "_pd_meas_2theta_range_min": 1,
        "_pd_meas_2theta_range_max": 140,
        "_pd_meas_2theta_range_inc": 0.05,
        "_phase": [
          {
            "_label": "SrTiO3",
            "_scale": 1
          }
        ],
        "_pd_background": [
          {
            "_2theta": 1,
            "_intensity": 20
          },
          {
            "_2theta": 140,
            "_intensity": 20
          }
        ]
      }
    }
  ]
}


# Tests

def test_simulation():
    desired = np.array([1.0, 2.0, 3.0])
    actual = np.array([1.1, 2.1, 3.1])
    #powder_mod.simulation(STUDY_DICT)
    pattern = powder_mod.simulation(STUDY_DICT)
    actual = pattern[1].astype(np.float64)
    assert_almost_equal(desired, actual, decimal=5, verbose=True)

def simulation():
    pattern = powder_mod.simulation(STUDY_DICT)
    y_calc = pattern[1].astype(np.float64)
    print("---", y_calc)

simulation()
