def get_index_dic():
    return {'Timestamp (s)': 0, 'Cost_Time (us)': 1, 'Alg_Cycle_Time (us)': 2, 'Ecat_Avg_Time (us)': 3, 'Ecat_Max_Time (us)': 4, 'Ecat_Min_Time (us)': 5, 'CPU_Rate (%)': 6, 'IMU_Time (s)': 7, 'Roll (deg)': 8, 'Pitch (deg)': 9, 'Yaw (deg)': 10, 'Roll_Vel (rad/s)': 11, 'Pitch_Vel (rad/s)': 12, 'Yaw_Vel (rad/s)': 13, 'X_Acc (m/s^2)': 14, 'Y_Acc (m/s^2)': 15, 'Z_Acc (m/s^2)': 16, 'Contact_Time (s)': 17, 'Contact_1': 18, 'Contact_2': 19, 'Contact_3': 20, 'Contact_4': 21, 'IN_FL_HipX_Ang (rad)': 22, 'IN_FL_HipY_Ang (rad)': 23, 'IN_FL_Knee_Ang (rad)': 24, 'IN_FR_HipX_Ang (rad)': 25, 'IN_FR_HipY_Ang (rad)': 26, 'IN_FR_Knee_Ang (rad)': 27, 'IN_HL_HipX_Ang (rad)': 28, 'IN_HL_HipY_Ang (rad)': 29, 'IN_HL_Knee_Ang (rad)': 30, 'IN_HR_HipX_Ang (rad)': 31, 'IN_HR_HipY_Ang (rad)': 32, 'IN_HR_Knee_Ang (rad)': 33, 'IN_FL_HipX_Vel (rad/s)': 34, 'IN_FL_HipY_Vel (rad/s)': 35, 'IN_FL_Knee_Vel (rad/s)': 36, 'IN_FR_HipX_Vel (rad/s)': 37, 'IN_FR_HipY_Vel (rad/s)': 38, 'IN_FR_Knee_Vel (rad/s)': 39, 'IN_HL_HipX_Vel (rad/s)': 40, 'IN_HL_HipY_Vel (rad/s)': 41, 'IN_HL_Knee_Vel (rad/s)': 42, 'IN_HR_HipX_Vel (rad/s)': 43, 'IN_HR_HipY_Vel (rad/s)': 44, 'IN_HR_Knee_Vel (rad/s)': 45, 'IN_FL_HipX_Tor (Nm)': 46, 'IN_FL_HipY_Tor (Nm)': 47, 'IN_FL_Knee_Tor (Nm)': 48, 'IN_FR_HipX_Tor (Nm)': 49, 'IN_FR_HipY_Tor (Nm)': 50, 'IN_FR_Knee_Tor (Nm)': 51, 'IN_HL_HipX_Tor (Nm)': 52, 'IN_HL_HipY_Tor (Nm)': 53, 'IN_HL_Knee_Tor (Nm)': 54, 'IN_HR_HipX_Tor (Nm)': 55, 'IN_HR_HipY_Tor (Nm)': 56, 'IN_HR_Knee_Tor (Nm)': 57, 'OUT_FL_HipX_Ang (rad)': 58, 'OUT_FL_HipY_Ang (rad)': 59, 'OUT_FL_Knee_Ang (rad)': 60, 'OUT_FR_HipX_Ang (rad)': 61, 'OUT_FR_HipY_Ang (rad)': 62, 'OUT_FR_Knee_Ang (rad)': 63, 'OUT_HL_HipX_Ang (rad)': 64, 'OUT_HL_HipY_Ang (rad)': 65, 'OUT_HL_Knee_Ang (rad)': 66, 'OUT_HR_HipX_Ang (rad)': 67, 'OUT_HR_HipY_Ang (rad)': 68, 'OUT_HR_Knee_Ang (rad)': 69, 'OUT_FL_HipX_Vel (rad/s)': 70, 'OUT_FL_HipY_Vel (rad/s)': 71, 'OUT_FL_Knee_Vel (rad/s)': 72, 'OUT_FR_HipX_Vel (rad/s)': 73, 'OUT_FR_HipY_Vel (rad/s)': 74, 'OUT_FR_Knee_Vel (rad/s)': 75, 'OUT_HL_HipX_Vel (rad/s)': 76, 'OUT_HL_HipY_Vel (rad/s)': 77, 'OUT_HL_Knee_Vel (rad/s)': 78, 'OUT_HR_HipX_Vel (rad/s)': 79, 'OUT_HR_HipY_Vel (rad/s)': 80, 'OUT_HR_Knee_Vel (rad/s)': 81, 'OUT_FL_HipX_Tor (Nm)': 82, 'OUT_FL_HipY_Tor (Nm)': 83, 'OUT_FL_Knee_Tor (Nm)': 84, 'OUT_FR_HipX_Tor (Nm)': 85, 'OUT_FR_HipY_Tor (Nm)': 86, 'OUT_FR_Knee_Tor (Nm)': 87, 'OUT_HL_HipX_Tor (Nm)': 88, 'OUT_HL_HipY_Tor (Nm)': 89, 'OUT_HL_Knee_Tor (Nm)': 90, 'OUT_HR_HipX_Tor (Nm)': 91, 'OUT_HR_HipY_Tor (Nm)': 92, 'OUT_HR_Knee_Tor (Nm)': 93, 'Scope_0': 94, 'Scope_1': 95, 'Scope_2': 96, 'Scope_3': 97, 'Scope_4': 98, 'Scope_5': 99, 'Scope_6': 100, 'Scope_7': 101, 'Scope_8': 102, 'Scope_9': 103, 'Scope_10': 104, 'Scope_11': 105, 'Scope_12': 106, 'Scope_13': 107, 'Scope_14': 108, 'Scope_15': 109, 'Scope_16': 110, 'Scope_17': 111, 'Scope_18': 112, 'Scope_19': 113, 'Scope_20': 114, 'Scope_21': 115, 'Scope_22': 116, 'Scope_23': 117, 'Scope_24': 118, 'Scope_25': 119, 'Scope_26': 120, 'Scope_27': 121, 'Scope_28': 122, 'Scope_29': 123, 'Scope_30': 124, 'Scope_31': 125, 'Scope_32': 126, 'Scope_33': 127, 'Scope_34': 128, 'Scope_35': 129, 'Scope_36': 130, 'Scope_37': 131, 'Scope_38': 132, 'Scope_39': 133, 'Scope_40': 134, 'Scope_41': 135, 'Scope_42': 136, 'Scope_43': 137, 'Scope_44': 138, 'Scope_45': 139, 'Scope_46': 140, 'Scope_47': 141, 'Scope_48': 142, 'Scope_49': 143, 'Scope_50': 144, 'Scope_51': 145, 'Scope_52': 146, 'Scope_53': 147, 'Scope_54': 148, 'Scope_55': 149, 'Scope_56': 150, 'Scope_57': 151, 'Scope_58': 152, 'Scope_59': 153, 'Scope_60': 154, 'Scope_61': 155, 'Scope_62': 156, 'Scope_63': 157, 'Scope_64': 158, 'Scope_65': 159, 'Scope_66': 160, 'Scope_67': 161, 'Scope_68': 162, 'Scope_69': 163, 'Scope_70': 164, 'Scope_71': 165, 'Scope_72': 166, 'Scope_73': 167, 'Scope_74': 168, 'Scope_75': 169, 'Scope_76': 170, 'Scope_77': 171, 'Scope_78': 172, 'Scope_79': 173, 'Scope_80': 174, 'Scope_81': 175, 'Scope_82': 176, 'Scope_83': 177, 'Scope_84': 178, 'Scope_85': 179, 'Scope_86': 180, 'Scope_87': 181, 'Scope_88': 182, 'Scope_89': 183, 'Scope_90': 184, 'Scope_91': 185, 'Scope_92': 186, 'Scope_93': 187, 'Scope_94': 188, 'Scope_95': 189, 'Scope_96': 190, 'Scope_97': 191, 'Scope_98': 192, 'Scope_99': 193, 'Scope_100': 194, 'Scope_101': 195, 'Scope_102': 196, 'Scope_103': 197, 'Scope_104': 198, 'Scope_105': 199, 'Scope_106': 200, 'Scope_107': 201, 'Scope_108': 202, 'Scope_109': 203, 'Scope_110': 204, 'Scope_111': 205, 'Scope_112': 206, 'Scope_113': 207, 'Scope_114': 208, 'Scope_115': 209, 'Scope_116': 210, 'Scope_117': 211, 'Scope_118': 212, 'Scope_119': 213, 'Scope_120': 214, 'Scope_121': 215, 'Scope_122': 216, 'Scope_123': 217, 'Scope_124': 218, 'Scope_125': 219, 'Scope_126': 220, 'Scope_127': 221, 'Scope_128': 222, 'Scope_129': 223, 'Scope_130': 224, 'Scope_131': 225, 'Scope_132': 226, 'Scope_133': 227, 'Scope_134': 228, 'Scope_135': 229, 'Scope_136': 230, 'Scope_137': 231, 'Scope_138': 232, 'Scope_139': 233, 'Scope_140': 234, 'Scope_141': 235, 'Scope_142': 236, 'Scope_143': 237, 'Scope_144': 238, 'Scope_145': 239, 'Scope_146': 240, 'Scope_147': 241, 'Scope_148': 242, 'Scope_149': 243, 'FL_HipX_Drive_Voltage (V)': 244, 'FL_HipY_Drive_Voltage (V)': 245, 'FL_Knee_Drive_Voltage (V)': 246, 'FR_HipX_Drive_Voltage (V)': 247, 'FR_HipY_Drive_Voltage (V)': 248, 'FR_Knee_Drive_Voltage (V)': 249, 'HL_HipX_Drive_Voltage (V)': 250, 'HL_HipY_Drive_Voltage (V)': 251, 'HL_Knee_Drive_Voltage (V)': 252, 'HR_HipX_Drive_Voltage (V)': 253, 'HR_HipY_Drive_Voltage (V)': 254, 'HR_Knee_Drive_Voltage (V)': 255, 'FL_HipX_Drive_Temp (C)': 256, 'FL_HipY_Drive_Temp (C)': 257, 'FL_Knee_Drive_Temp (C)': 258, 'FR_HipX_Drive_Temp (C)': 259, 'FR_HipY_Drive_Temp (C)': 260, 'FR_Knee_Drive_Temp (C)': 261, 'HL_HipX_Drive_Temp (C)': 262, 'HL_HipY_Drive_Temp (C)': 263, 'HL_Knee_Drive_Temp (C)': 264, 'HR_HipX_Drive_Temp (C)': 265, 'HR_HipY_Drive_Temp (C)': 266, 'HR_Knee_Drive_Temp (C)': 267, 'Motor_Temp_Time (s)': 268, 'FL_HipX_Motor_Temp (C)': 269, 'FL_HipY_Motor_Temp (C)': 270, 'FL_Knee_Motor_Temp (C)': 271, 'FR_HipX_Motor_Temp (C)': 272, 'FR_HipY_Motor_Temp (C)': 273, 'FR_Knee_Motor_Temp (C)': 274, 'HL_HipX_Motor_Temp (C)': 275, 'HL_HipY_Motor_Temp (C)': 276, 'HL_Knee_Motor_Temp (C)': 277, 'HR_HipX_Motor_Temp (C)': 278, 'HR_HipY_Motor_Temp (C)': 279, 'HR_Knee_Motor_Temp (C)': 280, 'Reserved_Motor_Temp (C)': 284}
    #下面的index 是tx JYB用的
    #return {'Timestamp (s)': 0, 'Cost_Time (us)': 1, 'IMU_Time (s)': 2, 'Roll (deg)': 3, 'Pitch (deg)': 4, 'Yaw (deg)': 5, 'Roll_Vel (rad/s)': 6, 'Pitch_Vel (rad/s)': 7, 'Yaw_Vel (rad/s)': 8, 'X_Acc (m/s^2)': 9, 'Y_Acc (m/s^2)': 10, 'Z_Acc (m/s^2)': 11, 'IN_FL_HipX_Ang (rad)': 12, 'IN_FL_HipY_Ang (rad)': 13, 'IN_FL_Knee_Ang (rad)': 14, 'IN_FR_HipX_Ang (rad)': 15, 'IN_FR_HipY_Ang (rad)': 16, 'IN_FR_Knee_Ang (rad)': 17, 'IN_HL_HipX_Ang (rad)': 18, 'IN_HL_HipY_Ang (rad)': 19, 'IN_HL_Knee_Ang (rad)': 20, 'IN_HR_HipX_Ang (rad)': 21, 'IN_HR_HipY_Ang (rad)': 22, 'IN_HR_Knee_Ang (rad)': 23, 'IN_FL_HipX_Vel (rad/s)': 24, 'IN_FL_HipY_Vel (rad/s)': 25, 'IN_FL_Knee_Vel (rad/s)': 26, 'IN_FR_HipX_Vel (rad/s)': 27, 'IN_FR_HipY_Vel (rad/s)': 28, 'IN_FR_Knee_Vel (rad/s)': 29, 'IN_HL_HipX_Vel (rad/s)': 30, 'IN_HL_HipY_Vel (rad/s)': 31, 'IN_HL_Knee_Vel (rad/s)': 32, 'IN_HR_HipX_Vel (rad/s)': 33, 'IN_HR_HipY_Vel (rad/s)': 34, 'IN_HR_Knee_Vel (rad/s)': 35, 'IN_FL_HipX_Tor (Nm)': 36, 'IN_FL_HipY_Tor (Nm)': 37, 'IN_FL_Knee_Tor (Nm)': 38, 'IN_FR_HipX_Tor (Nm)': 39, 'IN_FR_HipY_Tor (Nm)': 40, 'IN_FR_Knee_Tor (Nm)': 41, 'IN_HL_HipX_Tor (Nm)': 42, 'IN_HL_HipY_Tor (Nm)': 43, 'IN_HL_Knee_Tor (Nm)': 44, 'IN_HR_HipX_Tor (Nm)': 45, 'IN_HR_HipY_Tor (Nm)': 46, 'IN_HR_Knee_Tor (Nm)': 47, 'OUT_FL_HipX_Ang (rad)': 48, 'OUT_FL_HipY_Ang (rad)': 49, 'OUT_FL_Knee_Ang (rad)': 50, 'OUT_FR_HipX_Ang (rad)': 51, 'OUT_FR_HipY_Ang (rad)': 52, 'OUT_FR_Knee_Ang (rad)': 53, 'OUT_HL_HipX_Ang (rad)': 54, 'OUT_HL_HipY_Ang (rad)': 55, 'OUT_HL_Knee_Ang (rad)': 56, 'OUT_HR_HipX_Ang (rad)': 57, 'OUT_HR_HipY_Ang (rad)': 58, 'OUT_HR_Knee_Ang (rad)': 59, 'OUT_FL_HipX_Vel (rad/s)': 60, 'OUT_FL_HipY_Vel (rad/s)': 61, 'OUT_FL_Knee_Vel (rad/s)': 62, 'OUT_FR_HipX_Vel (rad/s)': 63, 'OUT_FR_HipY_Vel (rad/s)': 64, 'OUT_FR_Knee_Vel (rad/s)': 65, 'OUT_HL_HipX_Vel (rad/s)': 66, 'OUT_HL_HipY_Vel (rad/s)': 67, 'OUT_HL_Knee_Vel (rad/s)': 68, 'OUT_HR_HipX_Vel (rad/s)': 69, 'OUT_HR_HipY_Vel (rad/s)': 70, 'OUT_HR_Knee_Vel (rad/s)': 71, 'OUT_FL_HipX_Tor (Nm)': 72, 'OUT_FL_HipY_Tor (Nm)': 73, 'OUT_FL_Knee_Tor (Nm)': 74, 'OUT_FR_HipX_Tor (Nm)': 75, 'OUT_FR_HipY_Tor (Nm)': 76, 'OUT_FR_Knee_Tor (Nm)': 77, 'OUT_HL_HipX_Tor (Nm)': 78, 'OUT_HL_HipY_Tor (Nm)': 79, 'OUT_HL_Knee_Tor (Nm)': 80, 'OUT_HR_HipX_Tor (Nm)': 81, 'OUT_HR_HipY_Tor (Nm)': 82, 'OUT_HR_Knee_Tor (Nm)': 83, 'Scope_0': 84, 'Scope_1': 85, 'Scope_2': 86, 'Scope_3': 87, 'Scope_4': 88, 'Scope_5': 89, 'Scope_6': 90, 'Scope_7': 91, 'Scope_8': 92, 'Scope_9': 93, 'Scope_10': 94, 'Scope_11': 95, 'Scope_12': 96, 'Scope_13': 97, 'Scope_14': 98, 'Scope_15': 99, 'Scope_16': 100, 'Scope_17': 101, 'Scope_18': 102, 'Scope_19': 103, 'Scope_20': 104, 'Scope_21': 105, 'Scope_22': 106, 'Scope_23': 107, 'Scope_24': 108, 'Scope_25': 109, 'Scope_26': 110, 'Scope_27': 111, 'Scope_28': 112, 'Scope_29': 113, 'Scope_30': 114, 'Scope_31': 115, 'Scope_32': 116, 'Scope_33': 117, 'Scope_34': 118, 'Scope_35': 119, 'Scope_36': 120, 'Scope_37': 121, 'Scope_38': 122, 'Scope_39': 123, 'Scope_40': 124, 'Scope_41': 125, 'Scope_42': 126, 'Scope_43': 127, 'Scope_44': 128, 'Scope_45': 129, 'Scope_46': 130, 'Scope_47': 131, 'Scope_48': 132, 'Scope_49': 133, 'Scope_50': 134, 'Scope_51': 135, 'Scope_52': 136, 'Scope_53': 137, 'Scope_54': 138, 'Scope_55': 139, 'Scope_56': 140, 'Scope_57': 141, 'Scope_58': 142, 'Scope_59': 143, 'Scope_60': 144, 'Scope_61': 145, 'Scope_62': 146, 'Scope_63': 147, 'Scope_64': 148, 'Scope_65': 149, 'Scope_66': 150, 'Scope_67': 151, 'Scope_68': 152, 'Scope_69': 153, 'Scope_70': 154, 'Scope_71': 155, 'Scope_72': 156, 'Scope_73': 157, 'Scope_74': 158, 'Scope_75': 159, 'Scope_76': 160, 'Scope_77': 161, 'Scope_78': 162, 'Scope_79': 163, 'Scope_80': 164, 'Scope_81': 165, 'Scope_82': 166, 'Scope_83': 167, 'Scope_84': 168, 'Scope_85': 169, 'Scope_86': 170, 'Scope_87': 171, 'Scope_88': 172, 'Scope_89': 173, 'Scope_90': 174, 'Scope_91': 175, 'Scope_92': 176, 'Scope_93': 177, 'Scope_94': 178, 'Scope_95': 179, 'Scope_96': 180, 'Scope_97': 181, 'Scope_98': 182, 'Scope_99': 183, 'Scope_100': 184, 'Scope_101': 185, 'Scope_102': 186, 'Scope_103': 187, 'Scope_104': 188, 'Scope_105': 189, 'Scope_106': 190, 'Scope_107': 191, 'Scope_108': 192, 'Scope_109': 193, 'Scope_110': 194, 'Scope_111': 195, 'Scope_112': 196, 'Scope_113': 197, 'Scope_114': 198, 'Scope_115': 199, 'Scope_116': 200, 'Scope_117': 201, 'Scope_118': 202, 'Scope_119': 203, 'Scope_120': 204, 'Scope_121': 205, 'Scope_122': 206, 'Scope_123': 207, 'Scope_124': 208, 'Scope_125': 209, 'Scope_126': 210, 'Scope_127': 211, 'Scope_128': 212, 'Scope_129': 213, 'Scope_130': 214, 'Scope_131': 215, 'Scope_132': 216, 'Scope_133': 217, 'Scope_134': 218, 'Scope_135': 219, 'Scope_136': 220, 'Scope_137': 221, 'Scope_138': 222, 'Scope_139': 223, '': 224}