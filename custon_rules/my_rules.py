from gitlint.rules import CommitRule, RuleViolation

class BodyWithTwoParagraphs(CommitRule):
    
    name = "body-required-two-paragraphs"
    id = "UC2"
   
    def validate(self, commit):
        count = 0
        for line in commit.message.body:
            count += 1
            if count > 2:
                return

        return [RuleViolation(self.id, "Body has no paragraphs", line_nr=1)]