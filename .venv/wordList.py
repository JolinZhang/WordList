
Aninals = [
'Dog',	'Cow',	'Cat',	'Horse',
'Donkey',	'Tiger',	'Lion',	'Panther',
'Leopard',	'Cheetah',	'Bear',	'Elephant',
'Polar', 'bear','Turtle',	'Tortoise',	'Crocodile',
'Rabbit',	'Porcupine',	'Hare',	'Hen',
'Pigeon',	'Albatross',	'Crow',	'Fish',
'Dolphin' ,	'Frog',	'Whale'	,'Alligator',
'Eagle'	'Flying-squirrel'	,'Ostrich',	'Fox',
'Goat',	'Jackal',	'Emu','Armadillo',
'Eel',	'Goose',	'Arctic', 'fox',	'Wolf',
'Beagle',	'Gorilla',	'Chimpanzee',	'Monkey',
'Beaver',	'Orangutan',	'Antelope',	'Bat'
'Badger',	'Giraffe',	'Hermit-Crab',	'Giant-Panda',
'Hamster',	'Cobra',	'Hammerhead-shark',	'Camel',
'Hawk',	'Deer',	'Chameleon',	'Hippopotamus',
'Jaguar',	'Chihuahua',	'King-Cobra',	'Ibex',
'Lizard',	'Koala',	'Kangaroo',	'Iguana',
'Llama',	'Chinchillas',	'Dodo',	'Jellyfish',
'Rhinoceros',	'Hedgehog',	'Zebra',	'Possum',
'Wombat',	'Bison',	'Bull',	'Buffalo',
'Sheep',	'Meerkat',	'Mouse',	'Otter',
'Sloth',	'Owl',	'Vulture',	'Flamingo',
'Racoon',	'Mole',	'Duck',	'Swan',
'Lynx',	'Monitor', 'lizard',	'Elk',	'Boar',
'Lemur',	'Mule',	'Baboon',	'Mammoth','Blue-whale',	'Rat',	'Snake',	'Peacock'
]

Human = [
    'abdomen', 'anatomy','ankle','appendix', 'arch','arm','back','belly','belly-button',
    'bladder', 'blood-vessels','bone','bone', 'breast','buttocks', 'cell','cheek','chest',
    'chin','collar bone', 'digestive-system', 'ear','elbow','eyebrow','eyelashes', 'eyelid',
    'face','finger','forehead','fingernail','heart', 'heel', 'hip', 'intestines','index-finger',
    'jaw','kidney','knee','lip','lung','liver','muscle','molar', 'nostril', 'nipple','nerves','pinky','pelvis',
    'ribs','respiratory-system','shoulder','skin','spinal-cord','spine','stomach','teeth',
    'thorax','tissue', 'toe', 'tongue','tonsils', 'tooth','waist','wrist' 
]

Jobs = [
    'Accountant',
'Actor' ,'Actress',
'Architect',
'Artist',
'Astronaut',
'Athlete',
'Baker',
'Banker',
'Barber',
'Bartender',
'Biologist',
'Bookkeeper',
'Bricklayer',
'Bus-driver',
'Carpenter',
'Chef',
'Chemist',
'Civil engineer',
'Cleaner',
'Coach',
'Computer-programmer',
'Construction worker',
'Cook',
'Dancer',
'Dentist',
'Detective',
'Doctor',
'Economist',
'Electrician',
'Engineer',
'Farmer',
'Firefighter',
'Fisherman',
'Flight-attendant',
'Florist',
'Gardener',
'Graphic designer',
'Hairstylist',
'Historian',
'Housekeeper',
'Journalist',
'Judge',
'Lawyer',
'Librarian',
'Lifeguard',
'Mechanic',
'Musician',
'Nurse',
'Painter',
'Photographer',
]

Aninals_list = [s.capitalize().replace(" ", "-") for s in Aninals]
Human_list = [s.capitalize().replace(" ", "-") for s in Human]
Jobs_list = [s.capitalize().replace(" ", "-") for s in Jobs]
# check string eixst in list
merge_list = list(set(Aninals_list)| set(Human_list)|set(Jobs_list))
print(merge_list)





