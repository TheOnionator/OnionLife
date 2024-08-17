import random



WorldList = []
World_Food_Production = 100


def generate_initial_organisms(amount, world_list):

    Gene_Size = 10
    Gene_Movement_Speed = 10
    Gene_Metabolic_Rate = 10
    Gene_Reproduction_Rate = 10
    Gene_Mutation_Rate = 10

    x = range(amount)

    for n in x:
        world_list.append([])

        world_list[n].append([])
        world_list[n].append([])

        world_list[n][0].append("Size")
        world_list[n][0].append(Gene_Size)
        world_list[n][0].append("Movement_Speed")
        world_list[n][0].append(Gene_Movement_Speed)
        world_list[n][0].append("Metabolic_Rate")
        world_list[n][0].append(Gene_Metabolic_Rate)
        world_list[n][0].append("Reproduction_Rate")
        world_list[n][0].append(Gene_Reproduction_Rate)
        world_list[n][0].append("Mutation_Rate")
        world_list[n][0].append(Gene_Mutation_Rate)

        world_list[n][1].append("Health")
        world_list[n][1].append(Gene_Size*10)
        world_list[n][1].append("Food_Consumption")
        world_list[n][1].append((Gene_Size*Gene_Metabolic_Rate + Gene_Movement_Speed)/10)
        world_list[n][1].append("Food_Gathering")
        world_list[n][1].append((Gene_Size/5)*Gene_Movement_Speed)
        world_list[n][1].append("Max_Food_Bar")
        world_list[n][1].append(Gene_Size*50)
        world_list[n][1].append("Food_Bar")
        world_list[n][1].append(Gene_Size*50/2)
        world_list[n][1].append("Life_Span")
        world_list[n][1].append(400/Gene_Metabolic_Rate)
        world_list[n][1].append("Age")
        world_list[n][1].append(0)



generate_initial_organisms(10, WorldList)

print(WorldList)


def evolution(ticks, total_food_production, world_list):

    Time = range(ticks)
    World_Food_Consumption = 0

    for a in Time:
        starvation = 0
        old = 0

        for element in world_list:
            World_Food_Consumption += element[1][3]

        for element in world_list:

            element[1][13] += 1

            if element[1][9] + (element[1][5] - element[1][3]) <= 0:
                world_list.remove(element)
                starvation += 1
            if element[1][13] >= element[1][11]:
                world_list.remove(element)
                old += 1
            else:
                # if there is a surplus food in the world
                if total_food_production > World_Food_Consumption:
                    # if the food bar is less than max
                    if (element[1][9] + (element[1][5] - element[1][3])) < element[1][7]:
                        # add surplus food left over from consumption
                        element[1][9] += (element[1][5] - element[1][3])
                    # if the food bar is full
                    if (element[1][9] + (element[1][5] - element[1][3])) > element[1][7]:


                        Gene_Size = element[0][1]
                        Gene_Movement_Speed = element[0][3]
                        Gene_Metabolic_Rate = element[0][5]
                        Gene_Reproduction_Rate = element[0][7]
                        Gene_Mutation_Rate = element[0][9]





                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Size *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Size * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Size = 100
                        if Mutagen_Random == 2:
                            Gene_Size *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Size * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Size = 0.1

                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Movement_Speed *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Movement_Speed * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Movement_Speed = 100
                        if Mutagen_Random == 2:
                            Gene_Movement_Speed *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Size * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Movement_Speed = 0.1

                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Metabolic_Rate *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Metabolic_Rate * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Metabolic_Rate = 100
                        if Mutagen_Random == 2:
                            Gene_Metabolic_Rate *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Metabolic_Rate * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Metabolic_Rate = 0.1

                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Reproduction_Rate *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Reproduction_Rate * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Reproduction_Rate = 100
                        if Mutagen_Random == 2:
                            Gene_Reproduction_Rate *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Reproduction_Rate * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Reproduction_Rate = 0.1



                        world_list.append([])

                        n = len(world_list)-1

                        world_list[n].append([])
                        world_list[n].append([])

                        world_list[n][0].append("Size")
                        world_list[n][0].append(Gene_Size)
                        world_list[n][0].append("Movement_Speed")
                        world_list[n][0].append(Gene_Movement_Speed)
                        world_list[n][0].append("Metabolic_Rate")
                        world_list[n][0].append(Gene_Metabolic_Rate)
                        world_list[n][0].append("Reproduction_Rate")
                        world_list[n][0].append(Gene_Reproduction_Rate)
                        world_list[n][0].append("Mutation_Rate")
                        world_list[n][0].append(Gene_Mutation_Rate)


                        world_list[n][1].append("Health")
                        world_list[n][1].append(Gene_Size*10)
                        world_list[n][1].append("Food_Consumption")
                        world_list[n][1].append((Gene_Size*Gene_Metabolic_Rate + Gene_Movement_Speed)/10)
                        world_list[n][1].append("Food_Gathering")
                        world_list[n][1].append((Gene_Size/5)*Gene_Movement_Speed)
                        world_list[n][1].append("Max_Food_Bar")
                        world_list[n][1].append(Gene_Size*50)
                        world_list[n][1].append("Food_Bar")
                        world_list[n][1].append(Gene_Size*50/2)
                        world_list[n][1].append("Life_Span")
                        world_list[n][1].append(400/Gene_Metabolic_Rate)
                        world_list[n][1].append("Age")
                        world_list[n][1].append(0)

                        element[1][9] = Gene_Size*50/2



                if World_Food_Consumption > total_food_production:
                    # if the food bar is less than max
                    if (element[1][9] + (element[1][5] - element[1][3])) < element[1][7]:
                        # add surplus food left over from consumption
                        element[1][9] += ((element[1][5] - element[1][3]) * total_food_production/World_Food_Consumption)
                    # if the food bar is full
                    if (element[1][9] + (element[1][5] - element[1][3])) > element[1][7]:


                        Gene_Size = element[0][1]
                        Gene_Movement_Speed = element[0][3]
                        Gene_Metabolic_Rate = element[0][5]
                        Gene_Reproduction_Rate = element[0][7]
                        Gene_Mutation_Rate = element[0][9]





                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Size *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Size * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Size = 100
                        if Mutagen_Random == 2:
                            Gene_Size *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Size * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Size = 0.1

                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Movement_Speed *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Movement_Speed * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Movement_Speed = 100
                        if Mutagen_Random == 2:
                            Gene_Movement_Speed *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Size * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Movement_Speed = 0.1

                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Metabolic_Rate *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Metabolic_Rate * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Metabolic_Rate = 100
                        if Mutagen_Random == 2:
                            Gene_Metabolic_Rate *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Metabolic_Rate * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Metabolic_Rate = 0.1

                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Reproduction_Rate *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Reproduction_Rate * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Reproduction_Rate = 100
                        if Mutagen_Random == 2:
                            Gene_Reproduction_Rate *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Reproduction_Rate * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Reproduction_Rate = 0.1



                        world_list.append([])

                        n = len(world_list)-1

                        world_list[n].append([])
                        world_list[n].append([])

                        world_list[n][0].append("Size")
                        world_list[n][0].append(Gene_Size)
                        world_list[n][0].append("Movement_Speed")
                        world_list[n][0].append(Gene_Movement_Speed)
                        world_list[n][0].append("Metabolic_Rate")
                        world_list[n][0].append(Gene_Metabolic_Rate)
                        world_list[n][0].append("Reproduction_Rate")
                        world_list[n][0].append(Gene_Reproduction_Rate)
                        world_list[n][0].append("Mutation_Rate")
                        world_list[n][0].append(Gene_Mutation_Rate)


                        world_list[n][1].append("Health")
                        world_list[n][1].append(Gene_Size*10)
                        world_list[n][1].append("Food_Consumption")
                        world_list[n][1].append((Gene_Size*Gene_Metabolic_Rate + Gene_Movement_Speed)/10)
                        world_list[n][1].append("Food_Gathering")
                        world_list[n][1].append((Gene_Size/5)*Gene_Movement_Speed)
                        world_list[n][1].append("Max_Food_Bar")
                        world_list[n][1].append(Gene_Size*50)
                        world_list[n][1].append("Food_Bar")
                        world_list[n][1].append(Gene_Size*50/2)
                        world_list[n][1].append("Life_Span")
                        world_list[n][1].append(400/Gene_Metabolic_Rate)
                        world_list[n][1].append("Age")
                        world_list[n][1].append(0)

                        element[1][9] = Gene_Size*50/2





        print("Tick", a+1, " - ", len(world_list), "Creatures", World_Food_Consumption, "  ", starvation, "Died of Starvation  ", old, "Died of Old Age")
        World_Food_Consumption = 0
    print(world_list[-100])


evolution(1000, World_Food_Production, WorldList)
