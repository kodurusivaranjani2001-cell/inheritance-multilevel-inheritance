Code 1: Single Inheritance (phone_version → phone_version2)
phone_version has basic phone details and features (phone1a, phone2a methods).

phone_version2 inherits from phone_version, adds more features in phone1b.

In phone1b(), it first calls phone1a() (parent method) to get base features, then adds extra ones.

display() prints features from both parent and child.


Code 2: Multi-level Inheritance (first_gen → sec_gen → third_gen)
first_gen stores grandfather’s details.

sec_gen inherits from first_gen and adds father’s details.

third_gen inherits from sec_gen and adds child’s details.

super() is used in each class to call the parent’s __init__().

vars(traits) prints all attributes collected from all three generations.
