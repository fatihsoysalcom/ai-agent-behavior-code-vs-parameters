import random

def run_simulation(agent_func, input_score, threshold, noise_level, num_runs=5):
    """Helper to run an agent multiple times and show outcomes."""
    print(f"\n--- Running Agent: {agent_func.__name__} with Threshold={threshold:.2f}, Noise={noise_level:.2f} ---")
    decisions = []
    for i in range(num_runs):
        decision = agent_func(input_score, threshold, noise_level)
        decisions.append(decision)
        print(f"Run {i+1}: Input={input_score:.2f}, Decision='{decision}'")
    print(f"Summary of {num_runs} runs: {decisions.count('APPROVE')} APPROVE, {decisions.count('REJECT')} REJECT")
    return decisions

# --- Deterministic Software Example ---
def calculate_final_price_v1(base_price, discount_rate):
    """Calculates final price with a fixed discount rate (Version 1)."""
    # CODE CHANGE 1: Discount rate is 10%
    return base_price * (1 - discount_rate)

def calculate_final_price_v2(base_price, discount_rate):
    """Calculates final price with a slightly adjusted discount rate (Version 2)."""
    # CODE CHANGE 1: Discount rate is now 12%
    return base_price * (1 - discount_rate)

print("--- Deterministic Software: Code Diffs are Clear ---")
base_price = 100.0
print(f"V1 (10% discount): Final price for {base_price:.2f} is {calculate_final_price_v1(base_price, 0.10):.2f}")
print(f"V2 (12% discount): Final price for {base_price:.2f} is {calculate_final_price_v2(base_price, 0.12):.2f}")
print("Observation: A small code change (0.10 -> 0.12) directly and predictably alters the output.")

# --- AI Agent Example: Diffs are Insufficient ---

def simple_ai_agent_v1(feature_score, decision_threshold, noise_magnitude):
    """
    A simple AI-like agent making a decision with a stochastic element (Version 1).
    Simulates a model output + some inherent randomness.
    """
    # AI CONCEPT: Stochasticity - Add random noise to the score
    effective_score = feature_score + random.uniform(-noise_magnitude, noise_magnitude)
    
    # AI CONCEPT: Decision based on a 'model' (threshold)
    if effective_score >= decision_threshold:
        return "APPROVE"
    else:
        return "REJECT"

def simple_ai_agent_v2_code_change(feature_score, decision_threshold, noise_magnitude):
    """
    A simple AI-like agent with a *minor code change* in its internal logic (Version 2).
    The noise magnitude is slightly increased.
    """
    # AI CONCEPT: Small code change (noise_magnitude * 1.1)
    # This diff is small, but its behavioral impact can be complex and non-deterministic.
    effective_score = feature_score + random.uniform(-noise_magnitude * 1.1, noise_magnitude * 1.1)
    
    if effective_score >= decision_threshold:
        return "APPROVE"
    else:
        return "REJECT"

print("\n\n--- AI Agent: Code Diffs are Insufficient ---")

initial_feature_score = 0.55
initial_threshold = 0.60
initial_noise = 0.10

# Scenario 1: Base AI Agent Behavior
print("\n--- Scenario 1: Initial AI Agent (V1) Behavior ---")
run_simulation(simple_ai_agent_v1, initial_feature_score, initial_threshold, initial_noise, num_runs=10)
print("Observation: Due to randomness, the same input can yield different decisions over multiple runs.")

# Scenario 2: AI Agent - Small Code Change (V2)
print("\n--- Scenario 2: AI Agent (V2) with a small internal code change (increased noise) ---")
print("Code diff would show 'noise_magnitude' vs 'noise_magnitude * 1.1'.")
run_simulation(simple_ai_agent_v2_code_change, initial_feature_score, initial_threshold, initial_noise, num_runs=10)
print("Observation: A minor code change (10% more noise) can significantly alter the decision distribution,")
print("             and its full impact isn't obvious from just the diff; it requires behavioral testing.")


# Scenario 3: AI Agent - Hyperparameter Change (No Code Diff in function)
print("\n--- Scenario 3: AI Agent (V1) with a *hyperparameter change* (adjusted threshold) ---")
print("No code diff in 'simple_ai_agent_v1' function itself, only in its configuration/call.")
new_threshold = 0.50 # Changed from 0.60
run_simulation(simple_ai_agent_v1, initial_feature_score, new_threshold, initial_noise, num_runs=10)
print("Observation: Changing an external 'hyperparameter' (threshold) drastically changes behavior,")
print("             yet there is NO code diff in the agent's core logic. This is a key point of the article.")

# Scenario 4: AI Agent - Data Dependency (Simulated)
print("\n--- Scenario 4: AI Agent (V1) with a simulated 'data-driven' parameter change ---")
print("Imagine 'decision_threshold' was learned from training data.")
print("If the training data changed, the learned threshold might become 0.58.")
simulated_data_driven_threshold = 0.58
run_simulation(simple_ai_agent_v1, initial_feature_score, simulated_data_driven_threshold, initial_noise, num_runs=10)
print("Observation: A change in underlying 'training data' (simulated by changing the threshold here)")
print("             leads to behavioral changes without any code diff in the agent's logic.")
