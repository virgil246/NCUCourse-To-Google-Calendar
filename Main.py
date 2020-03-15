from QueryFromCourseSystem import Query
from parsing import parse_to_json

from googlecalender import main
if __name__ == "__main__":
    soup=Query()
    parse_to_json(soup)
    main()
    
    pass