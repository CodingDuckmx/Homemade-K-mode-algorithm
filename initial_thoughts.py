

'''
Core steps.

1.- Pick k observations or instances at random and use those as clusters.

2.- Compare each data point in the cluster to each observation data points.
    Any elements that are not equal we add 1 if they are equal nothing is added.

3.- Assign each individual to each centroid.

4.- Modify each centroid entry with the (statistic) mode of the observations associated with the chosen centroid.

5.- Repeat steps 2-4 until no changes are made in the assignment of individuals
    to the closest centroid.
'''

'''
It should be a class and should have fit and predict methods.
Numpy and Scipy are allowed to be used.

'''

################## Core step 0 ##################

# Import numpy, it will be needed

import numpy as np
import scipy.stats as stats

# Define the class (name and first attibutes).

class HomemadeKmode:
    def __init__(self,n_clusters = 1, max_iter=100):
        # Store the passed data.
        self.data = None
        # Set the number of clusters.
        self.n_clusters = n_clusters
        # Set the maximum number of iterations.
        self.max_iter = max_iter
        # Set a dictionary for storing the records.
        self.records = None

################## Core step 1 ##################

# 1.- Pick one observation or instance at random and use that as a cluster.
#   TODO Have a record of the tested combinations.

#   TODO make it functional to other data structures rather than pandas dataframe.

    def fit(self, data):
        
        self.data = data

        # Raise an error if the number of clusters is bigger than the number of observations.
        if self.n_clusters > len(self.data):

            raise NameError('The number of clusters must be shorter than the number of observations.')

        # Chose randomly our firsts clusters.
        self.clusters = {}
        # rand_index = [x for x in np.random.randint(0,len(self.data),self.n_clusters)]
        # for i in range(len(rand_index)):
        #     self.clusters[i] = [self.data[i],[]]

        #######################################################################################
        ############################## For development purposes ###############################
        #######################################################################################

        self.clusters = {0:[data[0],[]], 1:[data[-1],[]]}
        
        #######################################################################################
        #######################################################################################
        #######################################################################################


        # Prepare the records dictionary for storing the scores.

        # Need to store the discrepancies between the n-cluster and the m-element.
        # dictionary of records = {number_of_observation : {cluster_number: score (of discrepancies)}}
        self.records = {k:{l:0 for l in range(self.n_clusters)} for k in range(self.data.shape[0])}

################## Core step 2 ##################

# 2.- Compare each data point in the cluster to each observation data points.
#   Any elements that are not equal we add 1 if they are equal nothing is added.

        # for each cluster:
        for k in range(self.n_clusters):

            # for each row
            for i in range(self.data.shape[0]):

                # verify if the each element is the same with the cluster's same-place element
                for j in range(self.data.shape[1]):
                    if self.data[i][j] != self.clusters[k][0][j]:

                        self.records[i][k] += 1

        print(self.records)

################## Core step 3 ##################

# 3.- Assign each individual to each centroid.

        # for each record in records, chose the number with minimum value
        for key, value in self.records.items():

            # print(key, min(self.records[key], key=self.records[key].get) )
            self.clusters[min(self.records[key], key=self.records[key].get)][1].append(key)

        print(self.clusters)
################## Core step 4 ##################

# 4.- Each feature should have the (statistic) mode for each centroid.

        # for each cluster, reassign the values of the centroid with the modes.
        for cluster in self.clusters.values():

            cluster[0] = [stats.mode(self.data[cluster[1],i])[0][0] for i in range(self.data.shape[1]) ]


        print(self.clusters)


################## Core step 5 ##################

# 5.- Repeat steps 2-4 until no changes are made in the assignment of individuals
#       to the closest centroid.  


    def predict(self):

        for _ in range(self.max_iter):

            self.records = {k:{l:0 for l in range(self.n_clusters)} for k in range(self.data.shape[0])}

            for cluster in self.clusters.values():

                cluster[1] = []

            # for each cluster:
            for k in range(self.n_clusters):

                # for each row
                for i in range(self.data.shape[0]):

                    # verify if the each element is the same with the cluster's same-place element
                    for j in range(self.data.shape[1]):
                        if self.data[i][j] != self.clusters[k][0][j]:

                            self.records[i][k] += 1

            print(self.records)



            # for each record in records, chose the number with minimum value
            for key in self.records.keys():

                # print(key, min(self.records[key], key=self.records[key].get) )
                self.clusters[min(self.records[key], key=self.records[key].get)][1].append(key)


            for cluster in self.clusters.values():

                cluster[0] = [stats.mode(self.data[cluster[1],i])[0][0] for i in range(self.data.shape[1]) ]


            print(self.clusters)
        