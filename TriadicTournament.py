import random

#players classes
class supervisor:
    def __init__(self, supervisor_strategy):
        self.supervisor_strategy = supervisor_strategy

Sstrategy1 = supervisor("Sstrategy1")
Sstrategy2 = supervisor("Sstrategy2")
Sstrategy3 = supervisor("Sstrategy3")
SRandom = supervisor("SRandom")
Sself_Adjusting_Random = supervisor("Sself_Adjusting_Random")
STitfortat = supervisor("STitforTat")
SDefector = supervisor("SDefector")
SFixed = supervisor("SFixed")


class supervisee:
    def __init__(self, supervisee_strategy, partial_scores:list, trn_supervisee_score):
        self.supervisee_strategy = supervisee_strategy
        self.partial_scores = partial_scores
        self.trn_supervisee_score = trn_supervisee_score

Strategy1 = supervisee("Strategy1", [], 0)
Strategy2 = supervisee("Strategy2", [], 0)
Strategy3 = supervisee("Strategy3", [], 0)
Strategy4 = supervisee("Strategy4", [], 0)
Strategy5 = supervisee("Strategy5", [], 0)
Strategy6 = supervisee("Strategy6", [], 0)
Strategy7 = supervisee("Strategy7", [], 0)
Random = supervisee("Random", [], 0)
Self_Adjusting_Random = supervisee("Self_Adjusting_Random", [], 0)
TitforTat = supervisee("TitforTat", [], 0)
Defector = supervisee("Defector", [], 0)
Coworker = supervisee("Coworker", [], 0)
Cooperative = supervisee("Cooperative", [], 0)
Stakanov = supervisee("Stakanov", [], 0)


#lists
Supervisee_capacities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Partner_capacities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Cycles = [Strategy1, Strategy2, Strategy3, Strategy4, Strategy5, Strategy6, Strategy7, Random, Self_Adjusting_Random, TitforTat, Defector, Coworker, Cooperative, Stakanov]
Strategies = [Strategy1, Strategy2, Strategy3, Strategy4, Strategy5, Strategy6, Strategy7, Random, Self_Adjusting_Random, TitforTat, Defector, Coworker, Cooperative, Stakanov]
Tournament = [Sstrategy1, Sstrategy2, Sstrategy3, SRandom, Sself_Adjusting_Random, STitfortat, SDefector, SFixed]

#body
print("\n")
for supervisor in Tournament:
    strategy_supervisor_score=0
    for supervisee in Strategies:
        strategy_supervisee_score=0
        for partner in Cycles:
            cycle_supervisee_score=0
            cycle_supervisor_score=0
            for supervisee_capacity in Supervisee_capacities:
                capacity1=supervisee_capacity
                for partner_capacity in Partner_capacities:
                    capacity2=partner_capacity
                    upper_effort1 = 0
                    upper_effort2 = 0
                    level_effort1 = 0
                    level_effort2 = 0
                    previous_level_effort1 = 0
                    previous_level_effort2 = 0
                    previous_upper_effort1 = 0
                    previous_upper_effort2 = 0
                    wage1=0
                    wage2=0
                    previous_wage1 = 0
                    previous_previous_wage1 = 0
                    previous_wage2 = 0
                    previous_previous_wage2 = 0
                    alpha = random.random()
                    beta = random.random()
                    previous_score1 = 0
                    previous_score2 = 0
                    previous_previous_score1 = 0
                    previous_previous_score2 = 0
                    previous_sup_score = 0
                    previous_previous_sup_score = 0
                    incentive1 = 0
                    incentive2 = 0
                    previous_incentive1 = 0
                    previous_incentive2 = 0
                    numberofturns = #insert desired number of turns       
                    for i in range(numberofturns):
                        turn_supervisee_score=0
                        turn_supervisor_score=0
                        if supervisee.supervisee_strategy == "Strategy1":
                            if i == 1:
                                upper_effort1 = capacity1 / 100 * 50
                                level_effort1 = capacity1 / 100 * 40
                            else:
                                if previous_level_effort2 > (capacity1 / 100 * 50):
                                    upper_effort1 = capacity1 / 100 * 50
                                    level_effort1 = capacity1 / 100 * 40
                                elif previous_level_effort2 <= (capacity1 / 100 * 50):
                                    x = 30 + ((previous_level_effort2 * 100 / capacity1) / 5)
                                    level_effort1 = capacity1 / 100 * x
                                    upper_effort1 = capacity1 - level_effort1 - (capacity1 / 100 * 10)
                        elif supervisee.supervisee_strategy == "Strategy2":
                            if i == 1:
                                upper_effort1 = (capacity1 - (capacity1 / 100 * 40)) * (alpha / (alpha + beta))
                                level_effort1 = (capacity1 - (capacity1 / 100 * 40)) * (beta / (alpha + beta))
                            else:
                                if previous_level_effort2 < capacity1 / 100 * 20:
                                    upper_effort1 = (capacity1 - (capacity1 / 100 * 40)) * (alpha / (alpha + beta))
                                    level_effort1 = (capacity1 - (capacity1 / 100 * 40)) * (beta / (alpha + beta)) + (
                                                capacity1 / 100 * 20)
                                else:
                                    upper_effort1 = (capacity1 - (capacity1 / 100 * 40)) * (alpha / (alpha + beta))
                                    level_effort1 = (capacity1 - (capacity1 / 100 * 40)) * (beta / (alpha + beta))
                        elif supervisee.supervisee_strategy == "Strategy3":
                            if i < 3:
                                upper_effort1 = (capacity1 - (capacity1 / 100 * 20)) * (alpha / (alpha + beta))
                                level_effort1 = (capacity1 - (capacity1 / 100 * 20)) * (beta / (alpha + beta))
                            elif previous_previous_score1 <= previous_score1:
                                upper_effort1 = (capacity1 - (capacity1 / 100 * 20)) * (alpha / (alpha + beta))
                                level_effort1 = (capacity1 - (capacity1 / 100 * 20)) * (beta / (alpha + beta))
                            else:
                                upper_effort1 = previous_upper_effort1 + (previous_upper_effort1 / 100 * 10)
                                level_effort1 = (capacity1 - (capacity1 / 100 * 20)) - upper_effort1
                                if (capacity1 - (capacity1 / 100 * 20)) < upper_effort1:
                                    upper_effort1 = previous_upper_effort1
                                    level_effort1 = previous_level_effort1
                        elif supervisee.supervisee_strategy == "Strategy4":
                            if i == 1:
                                upper_effort1 = capacity1 / 100 * 20
                                level_effort1 = capacity1 / 100 * 20
                            else:
                                if previous_level_effort1 == (capacity1 / 100 * 40):
                                    if previous_level_effort2 < previous_level_effort1:
                                        level_effort1 = capacity1 / 100 * 30
                                    else:
                                        level_effort1 = capacity1 / 100 * 40
                                elif previous_level_effort1 == (capacity1 / 100 * 30):
                                    if previous_level_effort2 < previous_level_effort1:
                                        level_effort1 = capacity1 / 100 * 30
                                    else:
                                        level_effort1 = capacity1 / 100 * 40
                                elif previous_level_effort2 > previous_level_effort1:
                                    level_effort1 = capacity1 / 100 * 40
                                else:
                                    level_effort1 = capacity1 / 100 * 20
                                if i < 3:
                                    upper_effort1 = capacity1 / 100 * 20
                                elif previous_upper_effort1 == (capacity1 / 100 * 40):
                                    if previous_previous_score1 <= previous_score1:
                                        upper_effort1 = capacity1 / 100 * 30
                                    else:
                                        upper_effort1 = capacity1 / 100 * 40
                                    if previous_previous_score1 > previous_score1:
                                        upper_effort1 = capacity1 / 100 * 40
                                elif previous_upper_effort1 == (capacity1 / 100 * 30):
                                    if previous_previous_score1 <= previous_score1:
                                        upper_effort1 = capacity1 / 100 * 30
                                    else:
                                        upper_effort1 = capacity1 / 100 * 40
                                    if previous_previous_score1 > previous_score1:
                                        upper_effort1 = capacity1 / 100 * 40
                                elif previous_previous_score1 > previous_score1:
                                    upper_effort1 = capacity1 / 100 * 40
                                else:
                                    upper_effort1 = capacity1 / 100 * 20
                        elif supervisee.supervisee_strategy == "Strategy5":
                            if i == 1:
                                level_effort1 = capacity1 / 100 * 25
                                upper_effort1 = capacity1 / 100 * 25
                            else:
                                if previous_level_effort2 >= (capacity1 / 100 * 25):
                                    level_effort1 = capacity1 / 100 * 25
                                else:
                                    level_effort1 = previous_level_effort2
                                upper_effort1 = capacity1 - level_effort1 - (capacity1 / 100 * 25)
                        elif supervisee.supervisee_strategy == "Strategy6":
                            if i < 3:
                                upper_effort1 = (capacity1 - (capacity1 / 100 * 30)) * (alpha / (alpha + beta))
                                level_effort1 = (capacity1 - (capacity1 / 100 * 30)) * (beta / (alpha + beta))
                            else:
                                if previous_wage1 < previous_previous_wage1:
                                    if (capacity1 - previous_upper_effort1 - previous_level_effort1) < (
                                            capacity1 / 100 * 30):
                                        upper_effort1 = (capacity1 - (capacity1 / 100 * 20)) * (alpha / (alpha + beta))
                                        level_effort1 = (capacity1 - (capacity1 / 100 * 20)) * (beta / (alpha + beta))
                                    else:
                                        upper_effort1 = previous_upper_effort1 + (previous_upper_effort1 / 10)
                                        level_effort1 = previous_level_effort1 + (previous_level_effort1 / 10)
                                elif previous_wage1 >= previous_previous_wage1:
                                    if previous_score1 >= capacity1:
                                        upper_effort1 = previous_upper_effort1
                                        level_effort1 = previous_level_effort1
                                    else:
                                        upper_effort1 = previous_upper_effort1 - (previous_upper_effort1 / 10)
                                        level_effort1 = previous_level_effort1 - (previous_level_effort1 / 10)
                        elif supervisee.supervisee_strategy == "Strategy7":
                            if i < 3:
                                upper_effort1 = (capacity1 - (capacity1 / 100 * 30)) * (alpha / (alpha + beta))
                                level_effort1 = (capacity1 - (capacity1 / 100 * 30)) * (beta / (alpha + beta))
                            else:
                                if previous_previous_wage1 <= previous_wage1:
                                    upper_effort1 = previous_upper_effort1
                                    level_effort1 = previous_level_effort1
                                if previous_previous_wage1 > previous_wage1:
                                    if alpha == beta:
                                        upper_effort1 = previous_upper_effort1
                                        level_effort1 = previous_level_effort1
                                    elif alpha > beta:
                                        upper_effort1 = previous_upper_effort1 + (previous_upper_effort1 / 20)
                                        level_effort1 = previous_level_effort1 - (
                                                    upper_effort1 - previous_upper_effort1)
                                    else:
                                        level_effort1 = previous_level_effort1 + (previous_level_effort1 / 20)
                                        upper_effort1 = previous_upper_effort1 - (
                                                    level_effort1 - previous_level_effort1)
                                    if level_effort1 < 0 or level_effort1 > capacity1:
                                        level_effort1 = previous_level_effort1
                                    if upper_effort1 < 0 or upper_effort1 > capacity1:
                                        upper_effort1 = previous_upper_effort1
                        elif supervisee.supervisee_strategy == "Random":
                            xx = (random.randint(1, 100))
                            yy = (random.randint(1, 100))
                            zz = (random.randint(1, 100))
                            xyz = xx + yy + zz
                            xxx = xx / xyz
                            yyy = yy / xyz  # creating three random numbers and then diving them for their sum to make the resulting numbers add up to 1 so not to exceed available capacity
                            upper_effort1 = capacity1 * xxx
                            level_effort1 = capacity1 * yyy
                        elif supervisee.supervisee_strategy == "Self_Adjusting_Random":
                            if i < 3:
                                xx = (random.randint(1, 100))
                                yy = (random.randint(1, 100))
                                zz = (random.randint(1, 100))
                                xyz = xx + yy + zz
                                xxx = xx / xyz
                                yyy = yy / xyz
                                upper_effort1 = capacity1 * xxx
                                level_effort1 = capacity1 * yyy
                            else:
                                if previous_score1 < capacity1 or previous_score1 < previous_previous_score1:
                                    xx = (random.randint(1, 100))
                                    yy = (random.randint(1, 100))
                                    zz = (random.randint(1, 100))
                                    xyz = xx + yy + zz
                                    xxx = xx / xyz
                                    yyy = yy / xyz
                                    upper_effort1 = capacity1 * xxx
                                    level_effort1 = capacity1 * yyy
                                else:
                                    upper_effort1 = previous_upper_effort1
                                    level_effort1 = previous_level_effort1
                        elif supervisee.supervisee_strategy == "TitforTat":
                            if i == 1:
                                level_effort1 = (capacity1 - (capacity1 / 100 * 20)) * (beta / (alpha + beta))
                                upper_effort1 = (capacity1 - (capacity1 / 100 * 20)) * (alpha / (alpha + beta))
                            else:
                                level_effort1 = ((capacity1 - (capacity1 / 100 * 20)) * (
                                            beta / (alpha + beta)) + previous_level_effort2) / 2
                                if level_effort1 > (capacity1 - (capacity1 / 100 * 20) - (
                                        (capacity1 - (capacity1 / 100 * 20)) * (alpha / (alpha + beta)) / 100 * 70)):
                                    level_effort1 = (capacity1 - (capacity1 / 100 * 20) - (
                                                (capacity1 - (capacity1 / 100 * 20)) * (
                                                    alpha / (alpha + beta)) / 100 * 70))
                                if previous_wage1 > capacity1:
                                    if previous_wage1 >= previous_previous_wage1:
                                        upper_effort1 = (capacity1 - (capacity1 / 100 * 20)) * (
                                                    alpha / (alpha + beta)) + (
                                                                    capacity1 - (capacity1 - (capacity1 / 100 * 20)) * (
                                                                        alpha / (alpha + beta)) - level_effort1 - (
                                                                                capacity1 / 100 * 20))
                                    else:
                                        upper_effort1 = previous_upper_effort1 * (
                                                    previous_wage1 / previous_previous_wage1)
                                else:
                                    upper_effort1 = (capacity1 - (capacity1 / 100 * 20)) * (alpha / (alpha + beta)) / 2
                        elif supervisee.supervisee_strategy == "Defector":
                            upper_effort1 = (capacity1 / 100 * 30) + ((capacity1 - (capacity1 / 100 * 60)) * (alpha / (alpha + beta)))
                            level_effort1 = capacity1 - upper_effort1 - (capacity1 / 100 * 30)
                        elif supervisee.supervisee_strategy == "Coworker":
                            level_effort1 = (capacity1 / 100 * 30) + ((capacity1 - (capacity1 / 100 * 60)) * (beta / (alpha + beta)))
                            upper_effort1 = capacity1 - level_effort1 - (capacity1 / 100 * 30)
                        elif supervisee.supervisee_strategy == "Cooperative":
                            level_effort1 = (capacity1 - (capacity1 / 100 * 20)) * (beta / (beta + alpha))
                            upper_effort1 = (capacity1 - (capacity1 / 100 * 20)) * (alpha / (beta + alpha))
                        elif supervisee.supervisee_strategy == "Stakanov":
                            upper_effort1 = capacity1 * (alpha / (alpha + beta))
                            level_effort1 = capacity1 * (beta / (alpha + beta))

                        if partner.supervisee_strategy == "Strategy1":
                            if i == 1:
                                upper_effort2 = capacity2 / 100 * 50
                                level_effort2 = capacity2 / 100 * 40
                            else:
                                if previous_level_effort1 > (capacity2 / 100 * 50):
                                    upper_effort2 = capacity2 / 100 * 50
                                    level_effort2 = capacity2 / 100 * 40
                                elif previous_level_effort1 <= (capacity2 / 100 * 50):
                                    x = 30 + ((previous_level_effort1 * 100 / capacity2) / 5)
                                    level_effort2 = capacity2 / 100 * x
                                    upper_effort2 = capacity2 - level_effort2 - (capacity2 / 100 * 10)
                        elif partner.supervisee_strategy == "Strategy2":
                            if i == 1:
                                upper_effort2 = (capacity2 - (capacity2 / 100 * 40)) * (alpha / (alpha + beta))
                                level_effort2 = (capacity2 - (capacity2 / 100 * 40)) * (beta / (alpha + beta))
                            else:
                                if previous_level_effort1 < capacity2 / 100 * 20:
                                    upper_effort2 = (capacity2 - (capacity2 / 100 * 40)) * (alpha / (alpha + beta))
                                    level_effort2 = (capacity2 - (capacity2 / 100 * 40)) * (beta / (alpha + beta)) + (
                                                capacity2 / 100 * 20)
                                else:
                                    upper_effort2 = (capacity2 - (capacity2 / 100 * 40)) * (alpha / (alpha + beta))
                                    level_effort2 = (capacity2 - (capacity2 / 100 * 40)) * (beta / (alpha + beta))
                        elif partner.supervisee_strategy == "Strategy3":
                            if i < 3:
                                upper_effort2 = (capacity2 - (capacity2 / 100 * 20)) * (alpha / (alpha + beta))
                                level_effort2 = (capacity2 - (capacity2 / 100 * 20)) * (beta / (alpha + beta))
                            elif previous_previous_score2 <= previous_score2:
                                upper_effort2 = (capacity2 - (capacity2 / 100 * 20)) * (alpha / (alpha + beta))
                                level_effort2 = (capacity2 - (capacity2 / 100 * 20)) * (beta / (alpha + beta))
                            else:
                                upper_effort2 = previous_upper_effort2 + (previous_upper_effort2 / 100 * 10)
                                level_effort2 = (capacity2 - (capacity2 / 100 * 20)) - upper_effort2
                                if (capacity2 - (capacity2 / 100 * 20)) < upper_effort2:
                                    upper_effort2 = previous_upper_effort2
                                    level_effort2 = previous_level_effort2
                        elif partner.supervisee_strategy == "Strategy4":
                            if i == 1:
                                upper_effort2 = capacity2 / 100 * 20
                                level_effort2 = capacity2 / 100 * 20
                            else:
                                if previous_level_effort2 == (capacity2 / 100 * 40):
                                    if previous_level_effort1 < previous_level_effort2:
                                        level_effort2 = capacity2 / 100 * 30
                                    else:
                                        level_effort2 = capacity2 / 100 * 40
                                elif previous_level_effort2 == (capacity2 / 100 * 30):
                                    if previous_level_effort1 < previous_level_effort2:
                                        level_effort2 = capacity2 / 100 * 30
                                    else:
                                        level_effort2 = capacity2 / 100 * 40
                                elif previous_level_effort1 > previous_level_effort2:
                                    level_effort2 = capacity2 / 100 * 40
                                else:
                                    level_effort2 = capacity2 / 100 * 20
                                if i < 3:
                                    upper_effort2 = capacity2 / 100 * 20
                                elif previous_upper_effort2 == (capacity2 / 100 * 40):
                                    if previous_previous_score2 <= previous_score2:
                                        upper_effort2 = capacity2 / 100 * 30
                                    else:
                                        upper_effort2 = capacity2 / 100 * 40
                                    if previous_previous_score2 > previous_score2:
                                        upper_effort2 = capacity2 / 100 * 40
                                elif previous_upper_effort2 == (capacity2 / 100 * 30):
                                    if previous_previous_score2 <= previous_score2:
                                        upper_effort2 = capacity2 / 100 * 30
                                    else:
                                        upper_effort2 = capacity2 / 100 * 40
                                    if previous_previous_score2 > previous_score2:
                                        upper_effort2 = capacity2 / 100 * 40
                                elif previous_previous_score2 > previous_score2:
                                    upper_effort2 = capacity2 / 100 * 40
                                else:
                                    upper_effort2 = capacity2 / 100 * 20
                        elif partner.supervisee_strategy == "Strategy5":
                            if i == 1:
                                level_effort2 = capacity2 / 100 * 25
                                upper_effort2 = capacity2 / 100 * 25
                            else:
                                if previous_level_effort1 >= (capacity2 / 100 * 25):
                                    level_effort2 = capacity2 / 100 * 25
                                else:
                                    level_effort2 = previous_level_effort1
                                upper_effort2 = capacity2 - level_effort2 - (capacity2 / 100 * 25)
                        elif partner.supervisee_strategy == "Strategy6":
                            if i < 3:
                                upper_effort2 = (capacity2 - (capacity2 / 100 * 30)) * (alpha / (alpha + beta))
                                level_effort2 = (capacity2 - (capacity2 / 100 * 30)) * (beta / (alpha + beta))
                            else:
                                if previous_wage2 < previous_previous_wage2:
                                    if (capacity2 - previous_upper_effort2 - previous_level_effort2) < (
                                            capacity2 / 100 * 30):
                                        upper_effort2 = (capacity2 - (capacity2 / 100 * 20)) * (alpha / (alpha + beta))
                                        level_effort2 = (capacity2 - (capacity2 / 100 * 20)) * (beta / (alpha + beta))
                                    else:
                                        upper_effort2 = previous_upper_effort2 + (previous_upper_effort2 / 10)
                                        level_effort2 = previous_level_effort2 + (previous_level_effort2 / 10)
                                elif previous_wage2 >= previous_previous_wage2:
                                    if previous_score2 >= capacity2:
                                        upper_effort2 = previous_upper_effort2
                                        level_effort2 = previous_level_effort2
                                    else:
                                        upper_effort2 = previous_upper_effort2 - (previous_upper_effort2 / 10)
                                        level_effort2 = previous_level_effort2 - (previous_level_effort2 / 10)
                        elif partner.supervisee_strategy == "Strategy7":
                            if i < 3:
                                upper_effort2 = (capacity2 - (capacity2 / 100 * 30)) * (alpha / (alpha + beta))
                                level_effort2 = (capacity2 - (capacity2 / 100 * 30)) * (beta / (alpha + beta))
                            else:
                                if previous_previous_wage2 <= previous_wage2:
                                    upper_effort2 = previous_upper_effort2
                                    level_effort2 = previous_level_effort2
                                if previous_previous_wage2 > previous_wage2:
                                    if alpha == beta:
                                        upper_effort2 = previous_upper_effort2
                                        level_effort2 = previous_level_effort2
                                    elif alpha > beta:
                                        upper_effort2 = previous_upper_effort2 + (previous_upper_effort2 / 20)
                                        level_effort2 = previous_level_effort2 - (
                                                    upper_effort2 - previous_upper_effort2)
                                    else:
                                        level_effort2 = previous_level_effort2 + (previous_level_effort2 / 20)
                                        upper_effort2 = previous_upper_effort2 - (
                                                    level_effort2 - previous_level_effort2)
                                    if level_effort2 < 0 or level_effort2 > capacity2:
                                        level_effort2 = previous_level_effort2
                                    if upper_effort2 < 0 or upper_effort2 > capacity2:
                                        upper_effort2 = previous_upper_effort2
                        elif partner.supervisee_strategy == "Random":
                            xx = (random.randint(1, 100))
                            yy = (random.randint(1, 100))
                            zz = (random.randint(1, 100))
                            xyz = xx + yy + zz
                            xxx = xx / xyz
                            yyy = yy / xyz
                            upper_effort2 = capacity2 * xxx
                            level_effort2 = capacity2 * yyy
                        elif partner.supervisee_strategy == "Self_Adjusting_Random":
                            if i < 3:
                                xx = (random.randint(1, 100))
                                yy = (random.randint(1, 100))
                                zz = (random.randint(1, 100))
                                xyz = xx + yy + zz
                                xxx = xx / xyz
                                yyy = yy / xyz
                                upper_effort2 = capacity2 * xxx
                                level_effort2 = capacity2 * yyy
                            else:
                                if previous_score2 < capacity2 or previous_score2 < previous_previous_score2:
                                    xx = (random.randint(1, 100))
                                    yy = (random.randint(1, 100))
                                    zz = (random.randint(1, 100))
                                    xyz = xx + yy + zz
                                    xxx = xx / xyz
                                    yyy = yy / xyz
                                    upper_effort2 = capacity2 * xxx
                                    level_effort2 = capacity2 * yyy
                                else:
                                    upper_effort2 = previous_upper_effort2
                                    level_effort2 = previous_level_effort2
                        elif partner.supervisee_strategy == "TitforTat":
                            if i == 1:
                                level_effort2 = (capacity2 - (capacity2 / 100 * 20)) * (beta / (alpha + beta))
                                upper_effort2 = (capacity2 - (capacity2 / 100 * 20)) * (alpha / (alpha + beta))
                            else:
                                level_effort2 = ((capacity2 - (capacity2 / 100 * 20)) * (
                                            beta / (alpha + beta)) + previous_level_effort1) / 2
                                if level_effort2 > (capacity2 - (capacity2 / 100 * 20) - (
                                        (capacity2 - (capacity2 / 100 * 20)) * (alpha / (alpha + beta)) / 100 * 70)):
                                    level_effort2 = (capacity2 - (capacity2 / 100 * 20) - (
                                                (capacity2 - (capacity2 / 100 * 20)) * (
                                                    alpha / (alpha + beta)) / 100 * 70))
                                if previous_wage2 > capacity2:
                                    if previous_wage2 >= previous_previous_wage2:
                                        upper_effort2 = (capacity2 - (capacity2 / 100 * 20)) * (
                                                    alpha / (alpha + beta)) + (
                                                                    capacity2 - (capacity2 - (capacity2 / 100 * 20)) * (
                                                                        alpha / (alpha + beta)) - level_effort2 - (
                                                                                capacity2 / 100 * 20))
                                    else:
                                        upper_effort2 = previous_upper_effort2 * (
                                                    previous_wage2 / previous_previous_wage2)
                                else:
                                    upper_effort2 = (capacity2 - (capacity2 / 100 * 20)) * (alpha / (alpha + beta)) / 2
                        elif partner.supervisee_strategy == "Defector":
                            upper_effort2 = (capacity2 / 100 * 30) + ((capacity2 - (capacity2 / 100 * 60)) * (alpha / (alpha + beta)))
                            level_effort2 = capacity2 - upper_effort2 - (capacity2 / 100 * 30)
                        elif partner.supervisee_strategy == "Coworker":
                            level_effort2 = (capacity2 / 100 * 30) + ((capacity2 - (capacity2 / 100 * 60)) * (beta / (alpha + beta)))
                            upper_effort2 = capacity2 - level_effort2 - (capacity2 / 100 * 30)
                        elif partner.supervisee_strategy == "Cooperative":
                            level_effort2 = (capacity2 - (capacity2 / 100 * 20)) * (beta / (beta + alpha))
                            upper_effort2 = (capacity2 - (capacity2 / 100 * 20)) * (alpha / (beta + alpha))
                        elif partner.supervisee_strategy == "Stakanov":
                            upper_effort2 = capacity2 * (alpha / (alpha + beta))
                            level_effort2 = capacity2 * (beta / (alpha + beta))

                        turn_gross_productivity = ((upper_effort1+upper_effort2)**alpha)*((level_effort1+level_effort2)**beta)

                        if supervisor.supervisor_strategy== "Sstrategy1":
                            if i < 3:
                                incentive1 = 10
                                incentive2 = 10
                            else:
                                if previous_sup_score < previous_previous_sup_score:
                                    if upper_effort1 > upper_effort2:
                                        incentive1 = previous_incentive1 + 1
                                        incentive2 = previous_incentive2 - 1
                                    if upper_effort2 > upper_effort1:
                                        incentive1 = previous_incentive1 - 1
                                        incentive2 = previous_incentive2 + 1
                                    else:
                                        incentive1 = previous_incentive1
                                        incentive2 = previous_incentive2
                                    if incentive1 <= 0 or incentive2 <= 0:
                                        incentive1 = previous_incentive1
                                        incentive2 = previous_incentive2
                                else:
                                    incentive1 = previous_incentive1
                                    incentive2 = previous_incentive2
                            wage1 = turn_gross_productivity / 100 * incentive1
                            wage2 = turn_gross_productivity / 100 * incentive2
                        elif supervisor.supervisor_strategy== "Sstrategy2":
                            if i < 3:
                                incentive1 = 10
                                incentive2 = 10
                            else:
                                if previous_sup_score < previous_previous_sup_score:
                                    if alpha >= beta:
                                        if upper_effort1 > upper_effort2:
                                            incentive1 = previous_incentive1 + 1
                                            incentive2 = previous_incentive2 - 1
                                        if upper_effort2 > upper_effort1:
                                            incentive1 = previous_incentive1 - 1
                                            incentive2 = previous_incentive2 + 1
                                        else:
                                            incentive1 = previous_incentive1
                                            incentive2 = previous_incentive2
                                        if incentive1 <= 0 or incentive2 <= 0:
                                            incentive1 = previous_incentive1
                                            incentive2 = previous_incentive2
                                    else:
                                        if upper_effort1 > upper_effort2:
                                            incentive1 = previous_incentive1 - 1
                                            incentive2 = previous_incentive2 + 1
                                        if upper_effort2 > upper_effort1:
                                            incentive1 = previous_incentive1 + 1
                                            incentive2 = previous_incentive2 - 1
                                        else:
                                            incentive1 = previous_incentive1
                                            incentive2 = previous_incentive2
                                        if incentive1 <= 0 or incentive2 <= 0:
                                            incentive1 = previous_incentive1
                                            incentive2 = previous_incentive2
                                else:
                                    incentive1 = previous_incentive1
                                    incentive2 = previous_incentive2
                            wage1 = turn_gross_productivity / 100 * incentive1
                            wage2 = turn_gross_productivity / 100 * incentive2
                        elif supervisor.supervisor_strategy== "Sstrategy3":
                            if i < 3:
                                wage1 = turn_gross_productivity / 10
                                wage2 = turn_gross_productivity / 10
                            else:
                                if alpha > beta:
                                    if upper_effort1 >= previous_upper_effort1:
                                        wage1 = turn_gross_productivity / 10
                                    if upper_effort1 < previous_upper_effort1:
                                        wage1 = turn_gross_productivity / 20
                                    if upper_effort2 >= previous_upper_effort2:
                                        wage2 = turn_gross_productivity / 10
                                    if upper_effort2 < previous_upper_effort2:
                                        wage2 = turn_gross_productivity / 20
                                if alpha == beta:
                                    wage1 = turn_gross_productivity / 10
                                    wage2 = turn_gross_productivity / 10
                                else:
                                    if upper_effort1 > previous_upper_effort1:
                                        wage1 = turn_gross_productivity / 20
                                    if upper_effort1 <= previous_upper_effort1:
                                        wage1 = turn_gross_productivity / 10
                                    if upper_effort2 > previous_upper_effort2:
                                        wage2 = turn_gross_productivity / 20
                                    if upper_effort2 <= previous_upper_effort2:
                                        wage2 = turn_gross_productivity / 10
                        elif supervisor.supervisor_strategy== "SRandom":
                            xx = (random.randint(0, 40))
                            yy = (random.randint(0, 40))
                            wage1 = turn_gross_productivity / 100 * xx
                            wage2 = turn_gross_productivity / 100 * yy
                        elif supervisor.supervisor_strategy== "Sself_Adjusting_Random":
                            if i < 3:
                                incentive1 = (random.randint(0, 40))
                                incentive2 = (random.randint(0, 40))
                            else:
                                if previous_sup_score >= previous_previous_sup_score:
                                    incentive1 = previous_incentive1
                                    incentive2 = previous_incentive2
                                else:
                                    incentive1 = (random.randint(0, 40))
                                    incentive2 = (random.randint(0, 40))
                            wage1 = turn_gross_productivity / 100 * incentive1
                            wage2 = turn_gross_productivity / 100 * incentive2
                        elif supervisor.supervisor_strategy=="STitfortat":
                            if i < 3:
                                incentive1 = 10
                                incentive2 = 10
                            else:
                                if previous_sup_score >= previous_previous_sup_score:
                                    incentive1 = previous_incentive1 + 1
                                    incentive2 = previous_incentive2 + 1
                                else:
                                    incentive1 = previous_incentive1 - 1
                                    incentive2 = previous_incentive2 - 1
                                if alpha >= beta:
                                    if upper_effort1 >= previous_upper_effort1:
                                        if incentive1 >= 20:
                                            incentive1 = incentive1
                                        else:
                                            incentive1 = incentive1 + 1
                                    else:
                                        incentive1 = incentive1 - 1
                                    if upper_effort2 >= previous_upper_effort2:
                                        if incentive2 >= 20:
                                            incentive2 = incentive2
                                        else:
                                            incentive2 = incentive2 + 1
                                    else:
                                        incentive2 = incentive2 - 1
                                else:
                                    if upper_effort1 <= previous_upper_effort1:
                                        if incentive1 >= 20:
                                            incentive1 = incentive1
                                        else:
                                            incentive1 = incentive1 + 1
                                    else:
                                        incentive1 = incentive1 - 1
                                    if upper_effort2 <= previous_upper_effort2:
                                        if incentive2 >= 20:
                                            incentive2 = incentive2
                                        else:
                                            incentive2 = incentive2 + 1
                                    else:
                                        incentive2 = incentive2 - 1
                                if incentive1 < 1:
                                    incentive1 = 1
                                if incentive2 < 1:
                                    incentive2 = 1
                            wage1 = turn_gross_productivity / 100 * incentive1
                            wage2 = turn_gross_productivity / 100 * incentive2
                        elif supervisor.supervisor_strategy=="SDefector":
                            wage1 = turn_gross_productivity / 20
                            wage2 = turn_gross_productivity / 20
                        elif supervisor.supervisor_strategy=="SFixed":
                            wage1 = turn_gross_productivity / 10
                            wage2 = turn_gross_productivity / 10

                        if i > 2:
                            previous_previous_score1 = previous_score1
                            previous_previous_score2 = previous_score2
                            previous_previous_wage1 = previous_wage1
                            previous_previous_wage2 = previous_wage2
                            previous_previous_sup_score = previous_sup_score

                        previous_incentive1=incentive1
                        previous_incentive2=incentive2
                        previous_wage1=wage1
                        previous_wage2=wage2
                        previous_level_effort1=level_effort1
                        previous_level_effort2=level_effort2
                        previous_upper_effort1=upper_effort1
                        previous_upper_effort2=upper_effort2
                        turn_supervisee_score=wage1+(capacity1-upper_effort1-level_effort1)
                        turn_supervisee_score2=wage2+(capacity2-upper_effort2-level_effort2)
                        previous_score1=turn_supervisee_score
                        previous_score2=turn_supervisee_score2
                        turn_supervisor_score= turn_gross_productivity-wage1-wage2
                        previous_sup_score=turn_supervisor_score
                        cycle_supervisor_score=cycle_supervisor_score+turn_supervisor_score
                        cycle_supervisee_score=cycle_supervisee_score+turn_supervisee_score
            strategy_supervisee_score=strategy_supervisee_score+cycle_supervisee_score
            strategy_supervisor_score=strategy_supervisor_score+cycle_supervisor_score
        (supervisee.partial_scores).append(strategy_supervisee_score)

    print(supervisor.supervisor_strategy +"'s score is "+str(round(strategy_supervisor_score/1000/numberofturns))+"\n")

print("\n")
for supervisee in Strategies:
    for partial_score in supervisee.partial_scores:
        supervisee.trn_supervisee_score=supervisee.trn_supervisee_score + partial_score
    print(supervisee.supervisee_strategy + "'s score is "+str(round(supervisee.trn_supervisee_score/100/numberofturns)))
