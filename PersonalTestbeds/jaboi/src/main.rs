use std::error::Error;
use std::io;
use std::process;

use serde::Deserialize;

#[derive(Debug, Deserialize)]
struct DataRecord {
    id: u32,
    sepal_length: f32,
    sepal_width: f32,
    petal_length: f32,
    petal_width: f32,
    spieces: String,
}

fn read_csv() -> Result<(), Box<dyn Error>> {
    let mut reader = csv::Reader::from_reader(io::stdin());
    for result in reader.deserialize() {
        let record: DataRecord = result?;
        println!("{:?}", record);
    }
    Ok(())
}

fn main() {
    if let Err(e) = read_csv() {
        println!("we did an oopsie {:?}", e);
        process::exit(1);
    }
}