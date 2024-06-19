from matchpredictor.matchresults.result import Fixture, Outcome, Result, Team
from matchpredictor.predictors.predictor import Predictor, Prediction

class AlphabetPredictor(Predictor):

    def predict(self, fixture: Fixture) -> Prediction:
        hometeam = fixture.home_team.name
        awayteam = fixture.away_team.name
        
        if hometeam[0] > awayteam[0]:
            return Prediction(outcome=Outcome.HOME)
        elif hometeam[0] < awayteam[0]:
            return Prediction(outcome=Outcome.AWAY)
        else:
            return Prediction(outcome=Outcome.DRAW)
        
    