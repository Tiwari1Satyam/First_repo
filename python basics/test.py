def bayes_theorem(prior_A,prob_B_given_A, prob_B):
    return(prob_B_given_A* prior_A)/prob_B
priorsam=0.5
prioralex=0.3
probcrumbsGivensam=0.8
probcrumbsGivenalex=0.7
probcrumbs=0.6

posteriorsam=bayes_theorem(priorsam, probcrumbsGivensam,probcrumbs)
posterioralex=bayes_theorem(prioralex,probcrumbsGivenalex,probcrumbs)

print("posteriorsam:","%.2f"%posteriorsam)
print("posterioralex",posterioralex)

if posteriorsam>posterioralex:
    print("sam is suspect")
else:
    print("alex is suspect")

