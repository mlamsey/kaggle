use std::error::Error;
use std::io;
use std::process;
use std::vec::Vec;

use serde::Deserialize;

#[derive(Debug, Deserialize)]
struct DataRecord {
    Id: u32,
    SepalLengthCm: f32,
    SepalWidthCm: f32,
    PetalLengthCm: f32,
    PetalWidthCm: f32,
    Species: String,
}

fn parse_csv() -> Result<Vec<DataRecord>, Box<dyn Error>> {
    let mut reader = csv::Reader::from_reader(io::stdin());
    let mut records = Vec::new();
    for result in reader.deserialize() {
        let record: DataRecord = result?;
        println!("{:?}", record);
        records.push(record);
    }
    Ok(())
}

fn main() {
    let records = parse_csv().unwrap_or_else(|e| => {
        println!("Oopsie! {:?}", e);
        process::exit(1);
    }) 
}