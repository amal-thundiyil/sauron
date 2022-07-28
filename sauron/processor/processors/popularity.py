from sauron.processor.base_processor import BaseProcessor
from sauron.processor.metrics import  popularity

class PopularityProcessor(BaseProcessor):
    def summarize(self):
        data = {
            "watchers_count": self.backend.watchers_count,
            "stars_count": self.backend.stars_count,
            "followers_count": self.backend.followers_count,
            "reactions_count": self.backend.reactions_count,
            "dependents_count": self.backend.dependents_count,
        }
        res = {"score": popularity.summarize_score(data), "description": popularity.summarize_description(data)}
        return res

    def process(self):
        data = {
            "watchers_count": self.backend.watchers_count,
            "stars_count": self.backend.stars_count,
            "followers_count": self.backend.followers_count,
            "reactions_count": self.backend.reactions_count,
            "dependents_count": self.backend.dependents_count,
        }
        metrics = []
        scores = []
        descs = []
        for k, v in data.items():
            metrics.append(k) 
            scores.append(popularity.get_param_score(k, v))
            descs.append(popularity.get_param_description(k, v))
        return {"metrics": metrics, "score": scores, "description": descs}


