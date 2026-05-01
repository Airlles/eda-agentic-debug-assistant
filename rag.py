def load_knowledge_base(file_path):
  with open(file_path, "r") as file:
    knowledge_text = file.read()
  return knowledge_text

def split_into_sections(knowledge_text):
    raw_sections = knowledge_text.split("\n\n## ")

    sections = []

    for section in raw_sections:
        if section.startswith("# RTL"):
            continue

        sections.append(section)

    return sections

def retrieve_context(issue_type, knowledge_file="debug_knowledge.md"):
   knowledge_text = load_knowledge_base(knowledge_file)
   sections = split_into_sections(knowledge_text)

   for section in sections:
      section_title = section.splitlines()[0]

      if section_title == issue_type:
        return section
      






if __name__ == "__main__":
    context = retrieve_context("WIDTH_MISMATCH")
    print(context)