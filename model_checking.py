
abold = {"AI" : True,
"Machine" : True
}
rules = {
    "AI": ["IntelligentMachine", "Algorithm"],
    "Machine": ["Device", "IntelligentMachine"],
    "IntelligentMachine": ["SmartMachine", "LearningSystem"],
    "SmartMachine": ["RobotAssistant", "Mouad"],
    "Algorithm": ["SortingAlgorithm", "SearchAlgorithm"],
    "Device": ["Computer", "Smartphone"],
    "LearningSystem": ["NeuralNetwork", "ExpertSystem"],
    "Mouad": ["BestProgram"]
}

def Inference(rules,fact,mabe):
    sets = set()
    check_ste = set()
    if model_check(fact, rules,set(),mabe) == True:
        if fact in rules:
            check_ste.update(rules[fact])
        while check_ste :
            creant = check_ste.pop()
            if creant not in sets:
                sets.add(creant)
            if creant in rules:
                check_ste.update(rules[creant])
    return sets


def model_check(fact, rules,visit,mabe):
    if fact in abold and abold[fact] == True:
        return True
    if fact not in visit and fact in mabe:
        visit.add(fact)
        for facts in mabe[fact]:
                 result = model_check(facts, rules,visit,mabe)
                 if result == True:
                     return True
    return False
              
def infer_true_facts(fact,rules):#---->
    visit = set()
    mabe = {}
    fact_inf = []
    for parent in rules:
      for child in rules[parent]:
          if child not in mabe:
              mabe[child] = []
          mabe[child].append(parent)
    if model_check(fact, rules,set(),mabe)  == True:
       fact_inf = Inference(rules,fact,mabe)
       g = []
       g.append(fact)
       for facts in fact_inf:
         if model_check(facts, rules,set(),mabe)  == True:
             g.append(facts)
        
       return g
    return None
print(infer_true_facts("Mouad", rules))

        



                
                
                
              
            
     
                   

        
   
            
               
    
         
        
        







