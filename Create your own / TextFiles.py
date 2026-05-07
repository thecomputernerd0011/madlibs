import re
from collections import defaultdict

def parse_and_replace_file(input_file, output_file=None):
    """
    Parse a text file and replace words with user inputs.
    Uses regex-based word classification.
    
    Args:
        input_file (str): Path to the input .txt file
        output_file (str): Path to save the output (optional)
    
    Returns:
        str: The modified text
    """
    # Read the file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found. Self destructing in 5 seconds.")
        return None
    
    # Dictionary to store replacements for repeated words
    replacements = {}
    
    # Common verb endings (simplified classification)
    verb_patterns = [
        r'\b(run|walk|jump|is|are|was|were|be|have|has|had|do|does|did|go|goes|went|get|gets|got|make|makes|made|say|says|said|see|sees|saw|come|comes|came|take|takes|took|know|knows|knew|think|thinks|thought|find|finds|found|give|gives|gave|tell|tells|told|work|works|worked|call|calls|called|try|tries|tried|ask|asks|asked|need|needs|needed|feel|feels|felt|become|becomes|became|leave|leaves|left|put|puts|put|mean|means|meant|keep|keeps|kept|let|lets|let|begin|begins|began|seem|seems|seemed|help|helps|helped|talk|talks|talked|turn|turns|turned|start|starts|started|show|shows|showed|hear|hears|heard|play|plays|played|run|runs|ran)\b',
        r'\w+(ing|ed|s)$'  # -ing, -ed, -s endings
    ]
    
    # Common noun patterns
    noun_patterns = [
        r'\b(dog|cat|house|tree|person|man|woman|child|thing|time|way|day|year|world|life|hand|part|place|case|week|system|program|question|number|group|problem|fact|water|room|mother|father|family|school|government|company|business|service|money|side|head|eyes|ears|mouth|body|name|word|idea|city|country|friend|book|story|word|idea|town|road|street|river|mountain|sea|sky|sun|moon|star|flower|plant|food|bread|meat|fish|fruit|vegetable|drink|water|milk|coffee|tea|beer|wine|car|truck|train|plane|ship|boat|bike|horse|bird|snake|fish|insect|fish)\b',
        r'[A-Z][a-z]+(?:\s[A-Z][a-z]+)*'  # Capitalized words (proper nouns)
    ]
    
    # Common adjective patterns
    adjective_patterns = [
        r'\b(good|bad|big|small|hot|cold|fast|slow|happy|sad|beautiful|ugly|strong|weak|smart|stupid|kind|mean|nice|rude|clean|dirty|new|old|young|short|tall|heavy|light|hard|soft|wet|dry|sweet|bitter|sour|salty|red|blue|green|yellow|white|black|brown|pink|purple|orange|grey|dark|bright|quiet|loud|quick|slow|clever|dumb|brave|scared|angry|calm|gentle|rough|smooth|sharp|dull|bitter|sweet|salty|bitter|cheap|expensive|rich|poor|thick|thin|wide|narrow|deep|shallow|early|late|easy|difficult|simple|complex|rare|common|unique|normal|strange|special|ordinary|extraordinary|excellent|awful|wonderful|terrible|amazing|boring|fantastic|horrible|lovely|ugly|pleasant|unpleasant|delicious|disgusting|comfortable|uncomfortable|convenient|inconvenient|interesting|dull|exciting|boring|funny|serious|silly|wise|foolish|honest|dishonest|loyal|disloyal|faithful|unfaithful|courageous|cowardly|generous|selfish|humble|proud|modest|arrogant|yellow|blue|red|glitterly)\b',
        r'\w+(ful|less|able|ible|ous|ious|ious|al|ic|ical)$'  # -ful, -less, -able endings
    ]
    
    # Common proper nouns (Names)
    name_patterns = [
        r'\b(John|Mary|Michael|Sarah|David|Emma|Robert|Jessica|James|Lisa|William|Jennifer|Richard|Linda|Joseph|Barbara|Thomas|Patricia|Charles|Nancy|Daniel|Karen|Matthew|Lisa|Anthony|Betty|Donald|Margaret|Steven|Sandra|Paul|Ashley|Mark|Kimberly|Andrew|Donna|Kenneth|Michelle|Joshua|Dorothy|Kevin|Carol|Brian|Amanda|George|Melissa|Edward|Deborah|Ronald|Stephanie|Timothy|Rebecca|Jason|Sharon|Jeffrey|Laura|Ryan|Cynthia|Jacob|Kathleen|Gary|Amy|Nicholas|Angela|Eric|Shirley|Jonathan|Anna|Stephen|Brenda|Larry|Pamela|Justin|Emma|Scott|Nicole|Brandon|Helen|Benjamin|Samantha|Samuel|Katherine|Frank|Christine|Gregory|Debra|Alexander|Rachel|Raymond|Catherine|Patrick|Carolyn|Jack|Janet|Dennis|Ruth|Jerry|Maria|Tyler|Heather|Aaron|Diane|Jose|Julie|Adam|Joyce|Henry|Victoria|Zachary|Kelly|Douglas|Christina|Peter|Lauren|Kyle|Joan|Walter|Evelyn|Harold|Judith|Jeremy|Megan|Keith|Andrea|Christian|Cheryl|Roger|Hannah|Terry|Jacqueline|Sean|Martha|Austin|Madison|Gerald|Teresa|Carl|Gloria|Arthur|Sara|Ethan|Janice|Joe|Jean|Wyatt|Alice|Ralph|Abigail|Roy|Sophia|Russell|Judith|Louis|Rose)\b'
    ]
    
    def classify_word(word):
        """Classify a word as verb, noun, adjective, or name."""
        # Remove punctuation for classification
        clean_word = re.sub(r'[^\w]', '', word)
        
        if not clean_word:
            return(pattern, word):
                return 'name'
        
        # Check verb patterns
        for pattern in verb_patterns:
            if re.search(pattern, clean_word.lower()):
                return 'verb'
        
        # Check adjective patterns
        for pattern in adjective_patterns:
            if re.search(pattern, clean_word.lower()):
                return 'adjective'
        
        # Check noun patterns
        for pattern in noun_patterns:
            if re.search(pattern, clean_word.lower()):
                return 'noun'
        
        return None
    
    # Find all words and their positions
    word_pattern = r'\b\w+\b'
    words_found = list(re.finditer(word_pattern, text))
    
    # Process each word
    for match in words_found:
        word = match.group()
        word_lower = word.lower()
        
        # Only process if not already replaced
        if word_lower not in replacements:
            word_type = classify_word(word)
            
            if word_type:
                user_input = input(f"Replace '{word}' ({word_type}): ")
                replacements[word_lower] = user_input
    
    # Replace words in text
    def replace_word(match):
        word = match.group()
        replacement = replacements.get(word.lower())
        return replacement if replacement else word
    
    modified_text = re.sub(word_pattern, replace_word, text)
    
    # Save to output file if specified
    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(modified_text)
            print(f"\nOutput saved to '{output_file}'")
        except IOError as e:
            print(f"Error writing to file: {e}")
    
    return modified_text

def main():
    """Main function to run the word replacement program."""
    print("=" * 60)
    print("TEXT FILE WORD REPLACER")
    print("=" * 60)
    
    # Get input file path from user
    input_file = input("\nEnter the path to your .txt file: ").strip()
    
    if not input_file:
        print("No file path provided.")
        return
    
    output_file_input = input("Enter the output file path (or press Enter to skip): ").strip()
    output_file = output_file_input if output_file_input else None
    
    print("\nProcessing file...\n")
    result = parse_and_replace_file(input_file, output_file)
    
    if result:
        print("\n" + "=" * 60)
        print("Your MAd Lib:")
        print("=" * 60)
        print(result)
        print("=" * 60)

if __name__ == "__main__":
    main()
