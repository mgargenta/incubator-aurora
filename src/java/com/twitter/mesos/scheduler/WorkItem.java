package com.twitter.mesos.scheduler;

/**
 * Descriptions of the different types of external work items that task state machines may trigger.
 *
 * @author William Farner
 */
enum WorkItem {
  // Insert the task into the persistent store.
  CREATE_TASK,
  // Send an instruction for the runner of this task to kill the task.
  KILL,
  // Create a new state machine with a copy of this task.
  RESCHEDULE,
  // Update the task's state (schedule status) in the persistent store to match the state machine.
  UPDATE_STATE,
  // Delete this task from the persistent store.
  DELETE,
  // Increment the failure count for this task.
  INCREMENT_FAILURES
}