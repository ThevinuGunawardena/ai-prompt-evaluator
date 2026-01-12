from typing import List, Dict
import time

class PromptBenchmark:
    def __init__(self, prompt_template: str):
        self.template = prompt_template
        self.results: List[Dict] = []

    def log_run(self, duration_sec: float, token_count: int, cost_usd: float):
        self.results.append({
            "latency": duration_sec,
            "tokens": token_count,
            "cost": cost_usd
        })

    def summary(self) -> Dict:
        if not self.results:
            return {}
        avg_lat = sum(r["latency"] for r in self.results) / len(self.results)
        total_cost = sum(r["cost"] for r in self.results)
        return {"total_runs": len(self.results), "avg_latency": avg_lat, "total_cost": total_cost}
