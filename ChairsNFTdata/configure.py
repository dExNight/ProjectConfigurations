import json

rarity = {
    0: "Legendary",
    1: "Common",
    2: "Common",
    3: "Rare",
    4: "Rare",
    5: "Common",
    6: "Epic",
    7: "Rare",
    8: "Ultra Legendary"
}

for i in range(0, 9):
    name = f"Chair #{i+1}"
    description = "Inspired by the classic Eames chair, this chair is a perfect addition to any room."
    attributes = [{"trait_type": "Rarity", "value": rarity[i]}]
    image = f"https://github.com/Amir23714/ProjectConfigurations/blob/main/ChairsNFTdata/img/item_{i}.jpg"

    json_dict = {
        "name": name,
        "description": description,
        "attributes": attributes,
        "image": image
    }
    
    with open(f'item_{i}.json', 'w') as f:
        json.dump(json_dict, f)
    
    
