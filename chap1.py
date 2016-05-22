__author__ = 'X'
import recommendations
print(recommendations.critics['Gene Seymour'])
print(recommendations.critics['Mick LaSalle']['Snakes on a Plane'])
print(recommendations.sim_distance(recommendations.critics,'Lisa Rose', 'Gene Seymour'))

