from listqueue import ListQueue


def round_robin(job_queue):
    """ Each job in the job queue has a time slice of
    10 time units. An unfinished job will be returned
    to the rear of the queue. """

    while len(job_queue) != 0:
        currentJob = job_queue.pop()
        print(f'Current job: {currentJob}')

        currentJob -= 10

        if currentJob < 0:
            print('Job Finished')
        else:
            print('Job unfinised. Return to the rear of the queue')
            job_queue.add(currentJob)

        print(f'Job queue: {job_queue}')


def test_round_robin():
    job_list = [17, 5, 32, 8, 24]
    job_queue = ListQueue(job_list)
    print("Initial job queue:", job_queue)
    round_robin(job_queue)


test_round_robin()
