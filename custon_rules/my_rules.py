from gitlint.rules import CommitRule, RuleViolation

class BodyWithTwoParagraphs(CommitRule):
    
    name = "body-required-two-paragraphs"
    id = "UC2"
   
    def validate(self, commit):
        count = 0
        #print(commit.message.body)

        for line in commit.message.body:
            if (line == ''):
                count += 1

            if (count > 2 and line == 'See:'):
                return     

        return self.violation(self.id)

    def violation(self, id):
        return [RuleViolation(id, "Body needs to have at least two paragraphs", line_nr=1)]