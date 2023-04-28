from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Read the AI file
instructions = open("demofile.ai", "r").read()

# Prepare the AI
llm = OpenAI(temperature=0)

prompt = PromptTemplate(
    input_variables = ["instructions"],
    template = 
        """
        You are a code generation bot. Using the following instructions, output the corresponding code in Rust with no explanation.

        % INSTRUCTIONS:
        {instructions}
        """,
)

chain = LLMChain(llm = llm, prompt = prompt)

# Run the AI
code = chain.run(instructions)

# Write the code inside a file
f = open("demofile.rs", "w")
f.write(code)
f.close()

# Run rustc on the file
import os
os.system("rustc demofile.rs")

# Execute the resulting binary
os.system("./demofile")
