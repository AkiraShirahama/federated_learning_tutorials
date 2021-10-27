import flwr as fl
import pickle
from typing import List, Tuple, Optional
import os

class SaveModelStrategy(fl.server.strategy.FedAvg):
    def aggregate_fit(
        self,
        rnd: int,
        results: List[Tuple[fl.server.client_proxy.ClientProxy, fl.common.FitRes]],
        failures: List[BaseException],
    ) -> Optional[fl.common.Weights]:
        aggregated_weights = super().aggregate_fit(rnd, results, failures)
        if aggregated_weights is not None:
            # Save aggregated_weights
            print(f"Saving round {rnd} aggregated_weights...")
            with open(f"round-{rnd}-weights.pickle", 'wb') as f:
                pickle.dump(aggregated_weights, f)
        return aggregated_weights


init_param = None
if os.path.exists('round-3-weights.pickle'):
    with open('round-3-weights.pickle', 'rb') as f:
        init_weights = pickle.load(f)
    init_param = init_weights[0]

# Create strategy and run server
strategy = SaveModelStrategy(
    initial_parameters=init_param
)

fl.server.start_server(config={"num_rounds": 3}, force_final_distributed_eval=True, strategy=strategy)