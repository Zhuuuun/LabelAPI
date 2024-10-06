from fuzzywuzzy import fuzz

class FuzzyMatchError(Exception): 
    pass

class FuzzyService: 

    @staticmethod
    def fuzzy_string_match(correct: str, actual: str, threshold: int = 85) -> str:
        similiarityScore = fuzz.ratio(actual, correct)

        if similiarityScore >= threshold:
            return correct  
        else:
            raise FuzzyMatchError(f"String '{actual}' did not meet the similarity threshold with '{correct}'.")