import wikipediaapi

import appl
from appl import call, gen, ppl, records
from appl.const import NEWLINE

appl.init()
gen = appl.partial(gen, max_tokens=50, temperature=0.7)


def wikipedia(topic: str):
    wiki = wikipediaapi.Wikipedia(user_agent="APPL/0.1", language="en")
    page = wiki.page(topic)
    return wiki.extracts(page, exsentences=1)


@ppl
def query(topic: str):
    f"According to Wikipedia, {call(wikipedia, topic=topic)}"
    f"From my understanding, {topic} is {gen(stop=[NEWLINE])}"
    return records()


if __name__ == "__main__":
    print(query("apple"))
