# lib/owner_pet.py

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return all Pet instances belonging to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign a Pet instance to this Owner."""
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a list of this owner's pets sorted by pet name."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type

        # if owner is provided, validate it
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner class.")
        self.owner = owner

        # add instance to class variable
        Pet.all.append(self)
