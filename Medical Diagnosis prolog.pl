% Define the symptoms
symptom(fever).
symptom(cough).
symptom(headache).
symptom(sore_throat).
symptom(fatigue).

% Define the diseases
disease(influenza, [fever, cough, sore_throat, fatigue]).
disease(cold, [fever, headache, sore_throat]).
disease(measles, [fever, cough, sore_throat, rash]).

% Define the diagnose predicate
diagnose(Symptoms, Disease) :-
    disease(Disease, SymptomsList),
    subset(SymptomsList, Symptoms).

% Define the helper predicate subset/2 to check if a list of symptoms is a subset of another list
subset([], _).
subset([Head|Tail], List) :-
    member(Head, List),
    subset(Tail, List).
