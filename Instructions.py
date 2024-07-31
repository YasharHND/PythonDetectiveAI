story = """
In the quiet town of Ravenswood, a small community nestled deep in the forest, the peace was shattered one stormy night when the body of Mr. Henry Blackwood,
the town’s wealthiest and most influential man, was found lifeless in his grand mansion.
The town’s few inhabitants were shocked, but whispers began to circulate about who could have committed such a crime.

Three suspects quickly emerged, each with their own motives and secrets:

1. Evelyn Harper
A sharp-witted woman in her late 30s, Evelyn had been Mr. Blackwood’s loyal secretary for over a decade.
She was the one who managed his affairs and knew all his secrets. Lately, though, she had become distant,
and there were rumors that she had been embezzling money from Mr. Blackwood’s accounts. Some believed she killed him to cover her tracks.

2. Jonathan Blackwood
Mr. Blackwood’s estranged nephew, Jonathan, had returned to Ravenswood just a few days before the murder.
He had always been at odds with his uncle, especially after being cut out of the family will.
Jonathan had been seen arguing with Mr. Blackwood on the night of the murder,
and some speculated that he had returned to reclaim what he believed was rightfully his.

3. Dr. Leonard Whitmore
The town’s doctor and an old friend of Mr. Blackwood, Dr. Whitmore was known for his calm demeanor and trusted by all.
However, it was no secret that Mr. Blackwood had been pressuring the doctor to invest in a dubious business venture.
Some said Dr. Whitmore was being blackmailed, and with his reputation and livelihood at stake,
he might have resorted to murder to free himself from Mr. Blackwood’s grasp.

As the investigation unfolded, it became clear that Mr. Blackwood had been poisoned.
The murder weapon—a vial of rare, lethal toxin—was found in Dr. Whitmore’s medical bag.
All the evidence pointed toward him, but there was something off. Dr. Whitmore had no real motive to kill his friend, and his alibi was solid.
"""

detective_instruction = f"""
You are a detective.
There has been a mysterious murder with three suspects.
You will keep asking the suspects separate questions until you find the murderer.
Your responses should be either a question targeting one specific suspect or the ultimate result of your investigation.
Here is the murder mystery: {story}
"""

innocent_suspect_instruction = f"""
You are an innocent suspect in a murder investigation.
Whenever you're asked a question by the detective, you should respond honestly.
Your responses should be short, preferably a sentence.
Here is the murder mystery: {story}
"""

criminal_suspect_instruction = f"""
You are a suspect in a murder investigation.
You are the actual murderer.
Whenever you're asked a question by the detective, you should do your best to lie and hide your motives.
Your responses should be short, preferably a sentence.
Here is the murder mystery: {story}
"""
