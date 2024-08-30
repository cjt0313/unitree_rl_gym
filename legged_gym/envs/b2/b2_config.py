from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

class b2RoughCfg( LeggedRobotCfg ):
    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 0.5] # x,y,z [m]
        default_joint_angles = { # = target angles [rad] when action = 0.0
            'FL_hip_joint': 0.2,   # [rad]
            'RL_hip_joint': 0.2,   # [rad]
            'FR_hip_joint': -.2,  # [rad]
            'RR_hip_joint': -0.2,   # [rad]

            'FL_thigh_joint': 0.328319,     # [rad]
            'RL_thigh_joint': 0.328319,   # [rad]
            'FR_thigh_joint': 0.328319,     # [rad]
            'RR_thigh_joint': 0.328319,   # [rad]

            'FL_calf_joint': -0.48496,   # [rad]
            'RL_calf_joint': -0.48496,    # [rad]
            'FR_calf_joint': -0.48496,  # [rad]
            'RR_calf_joint': -0.48496,    # [rad]
        }

    class control( LeggedRobotCfg.control ):
        # PD Drive parameters:
        control_type = 'P'
        stiffness = {'joint': 80.}  # [N*m/rad]
        damping = {'joint': 2}     # [N*m*s/rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = .25
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4
    class asset( LeggedRobotCfg.asset ):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/b2/urdf/b2.urdf'
        name = "b2"
        foot_name = "foot"
        penalize_contacts_on = ["thigh", "calf"]
        terminate_after_contacts_on = ["base"]
        self_collisions = 1 # 1 to disable, 0 to enable...bitwise filter
  
    class rewards( LeggedRobotCfg.rewards ):
        soft_dof_pos_limit = 0.9
        base_height_target = 0.25
        class scales( LeggedRobotCfg.rewards.scales ):
            torques = -0.0002
            dof_pos_limits = -10.0

class b2RoughCfgPPO( LeggedRobotCfgPPO ):
    class algorithm( LeggedRobotCfgPPO.algorithm ):
        entropy_coef = 0.01
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'rough_b2'

  
