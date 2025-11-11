class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    all_persons = []

    for human in people:
        person = Person(human["name"], human["age"])
        all_persons.append(person)

    for human in people:

        if human.get("wife") and human["wife"] is not None:
            wife_obj = Person.people[human["wife"]]
            Person.people[human["name"]].wife = wife_obj

        elif human.get("husband") and human["husband"] is not None:
            husband_obj = Person.people[human["husband"]]
            Person.people[human["name"]].husband = husband_obj

    return all_persons
