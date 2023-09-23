import string
from collections import Counter

def count_words(paragraph):
    p1 = paragraph.lower()
    p1 = p1.translate(str.maketrans('', '', string.punctuation))
    allwords = p1.split()
    #alld = {k: p1.count(k) for k in allwords}
    alld = Counter(allwords)
    return alld


def main():
    paragraph = """Nadia’s Garden Restaurant is the creation of husband and wife team Nadia and Timothy Arbore. 
    Their American-infused, Italian-based, organically created, cuisine was inspired by Nadia’s papa, an immigrant from Italy, 
    who shared his love of cooking with Nadia as a young girl. His focus on using fresh ingredients and family style dining were 
    the inspiration for Nadia’s Garden Restaurant. Located in the heart of Main Streets Historic District, they are proud to be a 
    part of a rich community. In 2011, the duo remodeled the restaurant and updated their menu to include newer and more diverse entrées
     that could be made from local organic suppliers. Preservation of the building’s original layout has allowed them to create smaller, 
     more intimate, dining spaces. Nadia and Timothy are committed to sharing their family history of cuisine, along with their new inspirations,
      with their customers. Their passion for community, entertainment, and hospitality are found in every aspect of Nadia’s Garden Restaurant."""
    word_counts = (count_words(paragraph))

    s = word_counts.most_common(3)
    print(s)

if __name__ == "__main__":
    main()
