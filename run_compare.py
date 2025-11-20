from run_milp import main as milp_main
from run_cp_sat import main as cp_sat_main
from run_FJSP_DRL import main as fjsp_drl_main
from run_DANIEL import main as daniel_main
from run_genetic_algorithm import main as ga_main
from run_dispatching_rules import main as dispatch_main

def get_results(methods, config_files=None): # make sure the instance in each toml file is the same
    results = {}
    cfg = config_files or {}
    if 'milp' in methods:
        try:
            env = milp_main(param_file=cfg.get('milp', 'configs/milp.toml'))
            results['milp'] = env
        except Exception as e:
            results['milp'] = f"error: {e}"
    if 'cp_sat' in methods:
        try:
            env = cp_sat_main(param_file=cfg.get('cp_sat', 'configs/cp_sat.toml'))
            results['cp_sat'] = env
        except Exception as e:
            results['cp_sat'] = f"error: {e}"
    if 'fjsp_drl' in methods:
        try:
            env = fjsp_drl_main(param_file=cfg.get('fjsp_drl', 'configs/FJSP_DRL.toml'))
            results['fjsp_drl'] = env
        except Exception as e:
            results['fjsp_drl'] = f"error: {e}"
    if 'daniel' in methods:
        try:
            env = daniel_main(param_file=cfg.get('daniel', 'configs/DANIEL.toml'))
            results['daniel'] = env
        except Exception as e:
            results['daniel'] = f"error: {e}"
    if 'ga' in methods:
        try:
            best, env = ga_main(param_file=cfg.get('ga', 'configs/genetic_algorithm.toml'))
            results['ga'] = env
        except Exception as e:
            results['ga'] = f"error: {e}"
    if 'dispatch' in methods:
        try:
            env = dispatch_main(param_file=cfg.get('dispatch', 'configs/dispatching_rules.toml'))
            results['dispatch'] = env
        except Exception as e:
            results['dispatch'] = f"error: {e}"
    return results

def main(methods, config_files=None):
    results = get_results(methods, config_files)
    for method, env in results.items():
        try:
            print(f"{method}_makespan: {env.makespan}")
        except Exception:
            print(f"{method}_env: {env}")

if __name__ == "__main__":
    # methods = ['milp', 'cp_sat', 'fjsp_drl', 'daniel', 'ga', 'dispatch']
    methods = ['cp_sat', 'fjsp_drl', 'daniel', 'dispatch']
    main(methods)