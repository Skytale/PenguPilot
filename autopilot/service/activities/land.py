"""
  ___________________________________________________
 |  _____                       _____ _ _       _    |
 | |  __ \                     |  __ (_) |     | |   |
 | | |__) |__ _ __   __ _ _   _| |__) || | ___ | |_  |
 | |  ___/ _ \ '_ \ / _` | | | |  ___/ | |/ _ \| __| |
 | | |  |  __/ | | | (_| | |_| | |   | | | (_) | |_  |
 | |_|   \___|_| |_|\__, |\__,_|_|   |_|_|\___/ \__| |
 |                   __/ |                           |
 |  GNU/Linux based |___/  Multi-Rotor UAV Autopilot |
 |___________________________________________________|
 
 Landing Activity Class

 Copyright (C) 2014 Tobias Simon, Integrated Communication Systems Group, TU Ilmenau

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details. """


from time import sleep
from activity import Activity


class LandActivity(Activity):

   def __init__(self, autopilot):
      Activity.__init__(self, autopilot)

   def run(self):
      copter_height = 0.3
     
      ap = self.autopilot
      api = self.autopilot.api
      fsm = self.autopilot.fsm
      ultra_vp = ap.pse.data[0] + 0.5
      vp = min(ultra_vp, 2.0)
      api.set_vp(vp)
      while vp > -1.0:
         vp -= 0.025
         api.set_vp(vp)
         sleep(0.2)
         if ap.pse.data[0] < copter_height:
            vp = -1.2
      #disable ctrl outputs
      api.set_rp([0, 0])
      api.set_thrust(-10)
      api.mot_en(False)
      fsm.handle('done')

