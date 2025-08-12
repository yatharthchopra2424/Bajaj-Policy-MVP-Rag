import requests
import json
import time
import sys
import os
from datetime import datetime


# Define the API endpoint URL (replace with your actual ngrok or local URL, e.g., "http://localhost:8000/hackrx/run" or the ngrok public URL)
url = "https://1db8bd8b80b8.ngrok-free.app/"  # Update this with the actual URL where the FastAPI app is running
API_URL = f"{url}hackrx/run"  # Update this with the actual URL where the FastAPI app is running


def save_test_results(results, filename="test_results.json"):
    """Save test results to a JSON file for later analysis."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"📁 Test results saved to: {filename}")
    except Exception as e:
        print(f"⚠ Failed to save results: {e}")


def validate_api_url(url):
    """Check if the API URL is accessible."""
    try:
        # Simple GET request to check if the server is running
        response = requests.get(url.replace('/hackrx/run', '/'), timeout=10)
        return True
    except:
        return False


# Comprehensive list of test payloads for various document types and question scenarios
test_payloads = [
    
    # 1
    
    {
        "documents": "https://hackrx.blob.core.windows.net/assets/Test%20/Test%20Case%20HackRx.pptx?sv=2023-01-03&spr=https&st=2025-08-04T18%3A36%3A56Z&se=2026-08-05T18%3A36%3A00Z&sr=b&sp=r&sig=v3zSJ%2FKW4RhXaNNVTU9KQbX%2Bmo5dDEIzwaBzXCOicJM%3D",
        "questions": [
            "What is this ppt about?",
            "Can you summarize the key points of this presentation?",
            "Tell me about key coverage areas of this presentation."
        ]
    },

    # # 2

    # {
    # "documents": "https://hackrx.blob.core.windows.net/assets/policy.pdf?sv=2023-01-03&st=2025-07-04T09%3A11%3A24Z&se=2027-07-05T09%3A11%3A00Z&sr=b&sp=r&sig=N4a9OU0w0QXO6AOIBiu4bpl7AXvEZogeT%2FjUHNO7HzQ%3D",
    # "questions": [
    #     "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?",
    #     "What is the waiting period for pre-existing diseases (PED) to be covered?",
    #     "Does this policy cover maternity expenses, and what are the conditions?",
    #     "What is the waiting period for cataract surgery?",
    #     "Are the medical expenses for an organ donor covered under this policy?",
    #     "What is the No Claim Discount (NCD) offered in this policy?",
    #     "Is there a benefit for preventive health check-ups?",
    #     "How does the policy define a 'Hospital'?",
    #     "What is the extent of coverage for AYUSH treatments?",
    #     "Are there any sub-limits on room rent and ICU charges for Plan A?"
    #     ]
    # },

    # # 3

    # {
    #     "documents": "https://hackrx.blob.core.windows.net/assets/Happy%20Family%20Floater%20-%202024%20OICHLIP25046V062425%201.pdf?sv=2023-01-03&spr=https&st=2025-07-31T17%3A24%3A30Z&se=2026-08-01T17%3A24%3A00Z&sr=b&sp=r&sig=VNMTTQUjdXGYb2F4Di4P0zNvmM2rTBoEHr%2BnkUXIqpQ%3D",
    #     "questions": [
    #         "In the case of a multi-policy scenario, if the available coverage under the primary policy is less than the admissible claim amount, what is the procedure for claim settlement, coordination, and required documentation?",
    #         "While checking the process for submitting a dental claim for a 23-year-old financially dependent daughter (who recently married and changed her surname), also confirm the process for updating her last name in the policy records and provide the company's grievance redressal email.",
    #         "Suppose the insured's hospitalization was for evaluation and all tests and imaging were negative, leading to a decision for no treatment. Are these expenses claimable? Discuss using definitions and exclusions."
    #     ]
    # },

    # # 4

    # {
    #     "documents": "https://hackrx.blob.core.windows.net/assets/Arogya%20Sanjeevani%20Policy%20-%20CIN%20-%20U10200WB1906GOI001713%201.pdf?sv=2023-01-03&st=2025-07-21T08%3A29%3A02Z&se=2025-09-22T08%3A29%3A00Z&sr=b&sp=r&sig=nzrz1K9Iurt%2BBXom%2FB%2BMPTFMFP3PRnIvEsipAX10Ig4%3D",
    #     "questions": [
    #         "When will my root canal claim of Rs 25,000 be settled?",
    #         "I have done an IVF for Rs 56,000. Is it covered?",
    #         "I did a cataract treatment of Rs 100,000. Will you settle the full Rs 100,000?",
    #         "Give me a list of documents to be uploaded for hospitalization for heart surgery."
    #     ]
    # },

    # # 5

    {
        "documents": "https://hackrx.blob.core.windows.net/hackrx/rounds/News.pdf?sv=2023-01-03&spr=https&st=2025-08-07T17%3A10%3A11Z&se=2026-08-08T17%3A10%3A00Z&sr=b&sp=r&sig=ybRsnfv%2B6VbxPz5xF7kLLjC4ehU0NF7KDkXua9ujSf0%3D",
        "questions": [
            "ട്രംപ് ഏത് ദിവസമാണ് 100% ശുൽകം പ്രഖ്യാപിച്ചത്?",
            "What was Apple’s investment commitment and what was its objective?"
        ]
    },

    # # 6

    # {
    #     "documents": "https://hackrx.blob.core.windows.net/hackrx/rounds/News.pdf?sv=2023-01-03&spr=https&st=2025-08-07T17%3A10%3A11Z&se=2026-08-08T17%3A10%3A00Z&sr=b&sp=r&sig=ybRsnfv%2B6VbxPz5xF7kLLjC4ehU0NF7KDkXua9ujSf0%3D",
    #     "questions": [
    #         "What is my train number?"
    #     ]
    # },
    # {
    #     "documents": "https://hackrx.blob.core.windows.net/assets/Test%20/Test%20Case%20HackRx.pptx?sv=2023-01-03&spr=https&st=2025-08-04T18%3A36%3A56Z&se=2026-08-05T18%3A36%3A00Z&sr=b&sp=r&sig=v3zSJ%2FKW4RhXaNNVTU9KQbX%2Bmo5dDEIzwaBzXCOicJM%3D",
    #     "questions": [
    #         "What is the ideal spark plug gap recommeded",
    #         "Does this comes in tubeless tyre version",
    #         "Is it compulsoury to have a disc brake",
    #         "Can I put thums up instead of oil",
    #         "Give me JS code to generate a random number between 1 and 100"
    #     ]
    # },
    # {
    #     "documents": "https://hackrx.blob.core.windows.net/assets/Test%20/Mediclaim%20Insurance%20Policy.docx?sv=2023-01-03&spr=https&st=2025-08-04T18%3A42%3A14Z&se=2026-08-05T18%3A42%3A00Z&sr=b&sp=r&sig=yvnP%2FlYfyyqYmNJ1DX51zNVdUq1zH9aNw4LfPFVe67o%3D",
    #     "questions": [
    #         "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?",
    #         "What is the waiting period for pre-existing diseases (PED) to be covered?",
    #         "Does this policy cover maternity expenses, and what are the conditions?",
    #         "What is the waiting period for cataract surgery?",
    #         "Are the medical expenses for an organ donor covered under this policy?"
    #     ]
    # },
    # {
    #     "documents": "https://hackrx.blob.core.windows.net/assets/Test%20/Salary%20data.xlsx?sv=2023-01-03&spr=https&st=2025-08-04T18%3A46%3A54Z&se=2026-08-05T18%3A46%3A00Z&sr=b&sp=r&sig=sSoLGNgznoeLpZv%2FEe%2FEI1erhD0OQVoNJFDPtqfSdJQ%3D",
    #     "questions": [
    #         "What is the official name of India according to Article 1 of the Constitution?",
    #         "Which Article guarantees equality before the law and equal protection of laws to all persons?",
    #         "What is abolished by Article 17 of the Constitution?",
    #         "What are the key ideals mentioned in the Preamble of the Constitution of India?",
    #         "Under which Article can Parliament alter the boundaries, area, or name of an existing State?"
    #     ]
    # },
    # {
    #     "documents": "https://hackrx.blob.core.windows.net/assets/Test%20/Pincode%20data.xlsx?sv=2023-01-03&spr=https&st=2025-08-04T18%3A50%3A43Z&se=2026-08-05T18%3A50%3A00Z&sr=b&sp=r&sig=xf95kP3RtMtkirtUMFZn%2FFNai6sWHarZsTcvx8ka9mI%3D",
    #     "questions": [
    #         "If my car is stolen, what case will it be in law?",
    #         "If I am arrested without a warrant, is that legal?",
    #         "If someone denies me a job because of my caste, is that allowed?"
    #     ]
    # },
    {
        "documents": "https://hackrx.blob.core.windows.net/assets/Test%20/image.png?sv=2023-01-03&spr=https&st=2025-08-04T19%3A21%3A45Z&se=2026-08-05T19%3A21%3A00Z&sr=b&sp=r&sig=lAn5WYGN%2BUAH7mBtlwGG4REw5EwYfsBtPrPuB0b18M4%3D",
        "questions": [
            "How does Newton define 'quantity of motion' and how is it distinct from 'force'?",
            "According to Newton, what are the three laws of motion and how do they apply in celestial mechanics?",
            "How does Newton derive Kepler's Second Law (equal areas in equal times) from his laws of motion and gravitation?"
        ]
    },
    # {
    #     "documents": "https://hackrx.blob.core.windows.net/assets/Test%20/image.jpeg?sv=2023-01-03&spr=https&st=2025-08-04T19%3A29%3A01Z&se=2026-08-05T19%3A29%3A00Z&sr=b&sp=r&sig=YnJJThygjCT6%2FpNtY1aHJEZ%2F%2BqHoEB59TRGPSxJJBwo%3D",
    #     "questions": [
    #         "What is the ideal spark plug gap recommeded",
    #         "Does this comes in tubeless tyre version",
    #         "Is it compulsoury to have a disc brake",
    #         "Can I put thums up instead of oil",
    #         "Give me JS code to generate a random number between 1 and 100"
    #     ]
    # },
    # {
    #     "documents": "https://hackrx.blob.core.windows.net/assets/hackrx_pdf.zip?sv=2023-01-03&spr=https&st=2025-08-04T09%3A25%3A45Z&se=2027-08-05T09%3A25%3A00Z&sr=b&sp=r&sig=rDL2ZcGX6XoDga5%2FTwMGBO9MgLOhZS8PUjvtga2cfVk%3D",
    #     "questions": [
    #         "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?"
    #     ]
    # },
    # {
    #     "documents": "https://ash-speed.hetzner.com/10GB.bin",
    #     "questions": [
    #         "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?"
    #     ]
    # },
    # {
    #     "documents": "https://hackrx.blob.core.windows.net/assets/Test%20/Fact%20Check.docx?sv=2023-01-03&spr=https&st=2025-08-04T20%3A27%3A22Z&se=2028-08-05T20%3A27%3A00Z&sr=b&sp=r&sig=XB1%2FNzJ57eg52j4xcZPGMlFrp3HYErCW1t7k1fMyiIc%3D",
    #     "questions": [
    #         "If an insured person takes treatment for arthritis at home because no hospital beds are available, under what circumstances would these expenses NOT be covered, even if a doctor declares the treatment was medically required?",
    #         "A claim was lodged for expenses on a prosthetic device after a hip replacement surgery. The hospital bill also includes the cost of a walker and a lumbar belt post-discharge. Which items are payable?",
    #         "An insured's child (a dependent above 18 but under 26, unemployed and unmarried) requires dental surgery after an accident. What is the claim admissibility, considering both eligibility and dental exclusions, and what is the process for this specific scenario?",
    #         "If an insured undergoes Intra Operative Neuro Monitoring (IONM) during brain surgery, and also needs ICU care in a city over 1 million population, how are the respective expenses limited according to modern treatments, critical care definition, and policy schedule?",
    #         "A policyholder requests to add their newly-adopted child as a dependent. The child is 3 years old. What is the process and under what circumstances may the insurer refuse cover for the child, referencing eligibility and addition/deletion clauses?",
    #         "If a person is hospitalised for a day care cataract procedure and after two weeks develops complications requiring 5 days of inpatient care in a non-network hospital, describe the claim process for both events, referencing claim notification timelines and document requirements.",
    #         "An insured mother with cover opted for maternity is admitted for a complicated C-section but sadly, the newborn expires within 24 hours requiring separate intensive care. What is the claim eligibility for the newborn's treatment expenses, referencing definitions, exclusions, and newborn cover terms?"
    #     ]
    # }

]


def test_api_endpoint(payloads_to_test=None):
    """
    Comprehensive test function for the HackRX API endpoint.
    Tests various document types and question scenarios with detailed logging.
    
    Args:
        payloads_to_test: List of payloads to test. If None, uses global test_payloads.
    
    Returns:
        dict: Structured test results with all questions and answers
    """
    if payloads_to_test is None:
        payloads_to_test = test_payloads
    
    total_tests = len(payloads_to_test)
    successful_tests = 0
    failed_tests = 0
    total_questions = sum(len(payload['questions']) for payload in payloads_to_test)
    
    # Initialize structured results
    test_results = {
        "test_summary": {
            "total_tests": total_tests,
            "total_questions": total_questions,
            "api_endpoint": API_URL,
            "test_started": time.strftime('%Y-%m-%d %H:%M:%S'),
            "successful_tests": 0,
            "failed_tests": 0,
            "success_rate": 0.0,
            "total_duration": 0.0,
            "average_time_per_test": 0.0
        },
        "test_cases": []
    }
    
    print(f"\n{'='*80}")
    print(f"🚀 STARTING COMPREHENSIVE API TESTING")
    print(f"{'='*80}")
    print(f"📊 Total Test Payloads: {total_tests}")
    print(f"📝 Total Questions: {total_questions}")
    print(f"🔗 API Endpoint: {API_URL}")
    print(f"⏰ Test Started: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*80}\n")
    
    start_time = time.time()
    
    for idx, payload in enumerate(payloads_to_test, start=1):
        print(f"\n{'='*60}")
        print(f"🧪 TEST CASE {idx}/{total_tests}")
        print(f"{'='*60}")
        
        # Extract document type from URL for better categorization
        doc_url = payload['documents']
        if 'policy.pdf' in doc_url:
            doc_type = "🏥 Insurance Policy (National Parivar Mediclaim)"
            doc_category = "Insurance"
        elif 'Happy%20Family%20Floater' in doc_url:
            doc_type = "👨‍👩‍👧‍👦 Family Floater Insurance"
            doc_category = "Insurance"
        elif 'Arogya%20Sanjeevani' in doc_url:
            doc_type = "🩺 Arogya Sanjeevani Policy"
            doc_category = "Insurance"
        elif 'UNI%20GROUP' in doc_url:
            doc_type = "🏢 Group Health Insurance"
            doc_category = "Insurance"
        elif 'principia_newton' in doc_url:
            doc_type = "🔬 Newton's Principia (Scientific)"
            doc_category = "Scientific"
        elif 'indian_constitution' in doc_url:
            doc_type = "🏛 Indian Constitution (Legal)"
            doc_category = "Legal"
        elif 'Super_Splendor' in doc_url:
            doc_type = "🏍 Motorcycle Manual (Technical)"
            doc_category = "Technical"
        else:
            doc_type = "📄 Document"
            doc_category = "Unknown"
        
        # Initialize test case result
        test_case_result = {
            "test_case_id": idx,
            "document_type": doc_type,
            "document_category": doc_category,
            "document_url": doc_url,
            "total_questions": len(payload['questions']),
            "test_started": time.strftime('%H:%M:%S'),
            "status": "pending",
            "processing_time": 0.0,
            "avg_time_per_question": 0.0,
            "error_message": None,
            "questions_and_answers": []
        }
            
        print(f"📋 Document Type: {doc_type}")
        print(f"🔗 Document URL: {doc_url}")
        print(f"❓ Number of Questions: {len(payload['questions'])}")
        print(f"⏱  Test Started: {time.strftime('%H:%M:%S')}")
        
        test_start_time = time.time()
        
        try:
            print(f"\n📤 Sending request to API...")
            response = requests.post(API_URL, json=payload, timeout=300)  # 5-minute timeout
            response.raise_for_status()
            result = response.json()
            
            test_duration = time.time() - test_start_time
            
            if "error" in result:
                print(f"\n❌ API ERROR: {result['error']}")
                failed_tests += 1
                test_case_result["status"] = "failed"
                test_case_result["error_message"] = result['error']
                test_case_result["processing_time"] = test_duration
            else:
                print(f"\n✅ SUCCESS! Received {len(result.get('answers', []))} answers")
                print(f"⏱  Processing Time: {test_duration:.2f} seconds")
                print(f"📊 Avg Time per Question: {test_duration/len(payload['questions']):.2f} seconds")
                
                successful_tests += 1
                test_case_result["status"] = "success"
                test_case_result["processing_time"] = test_duration
                test_case_result["avg_time_per_question"] = test_duration/len(payload['questions'])
                
                # Store questions and answers in structured format
                for q_idx, (question, answer) in enumerate(zip(payload['questions'], result.get('answers', [])), 1):
                    test_case_result["questions_and_answers"].append({
                        "question_id": q_idx,
                        "question": question,
                        "answer": answer
                    })
                
                # Display questions and answers with better formatting
                print(f"\n{'─'*50}")
                print("📝 QUESTIONS & ANSWERS:")
                print(f"{'─'*50}")
                
                for qa in test_case_result["questions_and_answers"]:
                    print(f"\n🔍 Q{qa['question_id']}: {qa['question']}")
                    print(f"💡 A{qa['question_id']}: {qa['answer']}")
                    
                    # Add separator between Q&A pairs
                    if qa['question_id'] < len(payload['questions']):
                        print(f"{'·'*40}")
            
        except requests.exceptions.Timeout:
            print(f"\n⏰ TIMEOUT ERROR: Request took longer than 5 minutes")
            failed_tests += 1
            test_case_result["status"] = "failed"
            test_case_result["error_message"] = "Request timeout (5 minutes)"
            test_case_result["processing_time"] = time.time() - test_start_time
        except requests.exceptions.ConnectionError:
            print(f"\n🌐 CONNECTION ERROR: Unable to connect to API endpoint")
            failed_tests += 1
            test_case_result["status"] = "failed"
            test_case_result["error_message"] = "Connection error - unable to connect to API endpoint"
            test_case_result["processing_time"] = time.time() - test_start_time
        except requests.exceptions.HTTPError as e:
            print(f"\n🚫 HTTP ERROR: {e}")
            try:
                print(f"Response Status Code: {e.response.status_code}")
                print(f"Response Text: {e.response.text[:500]}...")
                error_details = f"HTTP {e.response.status_code}: {e.response.text[:200]}..."
            except:
                error_details = f"HTTP Error: {str(e)}"
                print("Could not retrieve response details")
            failed_tests += 1
            test_case_result["status"] = "failed"
            test_case_result["error_message"] = error_details
            test_case_result["processing_time"] = time.time() - test_start_time
        except requests.exceptions.RequestException as e:
            print(f"\n💥 REQUEST ERROR: {e}")
            failed_tests += 1
            test_case_result["status"] = "failed"
            test_case_result["error_message"] = f"Request error: {str(e)}"
            test_case_result["processing_time"] = time.time() - test_start_time
        except json.JSONDecodeError:
            print(f"\n📝 JSON DECODE ERROR: Invalid JSON response")
            failed_tests += 1
            test_case_result["status"] = "failed"
            test_case_result["error_message"] = "Invalid JSON response from API"
            test_case_result["processing_time"] = time.time() - test_start_time
        except Exception as e:
            print(f"\n🔥 UNEXPECTED ERROR: {e}")
            failed_tests += 1
            test_case_result["status"] = "failed"
            test_case_result["error_message"] = f"Unexpected error: {str(e)}"
            test_case_result["processing_time"] = time.time() - test_start_time
        
        # Add test case result to results
        test_results["test_cases"].append(test_case_result)
        
        # Progress indicator
        progress = (idx / total_tests) * 100
        print(f"\n📈 Progress: {progress:.1f}% ({idx}/{total_tests} tests completed)")
        
        # Add delay between tests to avoid overwhelming the API
        if idx < total_tests:  # Don't delay after the last test
            print(f"⏳ Waiting 5 seconds before next test...")
            time.sleep(5)
    
    # Final summary
    total_duration = time.time() - start_time
    
    # Update test results summary
    test_results["test_summary"].update({
        "successful_tests": successful_tests,
        "failed_tests": failed_tests,
        "success_rate": (successful_tests/total_tests)*100 if total_tests > 0 else 0.0,
        "total_duration": total_duration,
        "average_time_per_test": total_duration/total_tests if total_tests > 0 else 0.0,
        "test_completed": time.strftime('%Y-%m-%d %H:%M:%S')
    })
    
    print(f"\n{'='*80}")
    print(f"🏁 TESTING COMPLETED")
    print(f"{'='*80}")
    print(f"📊 SUMMARY STATISTICS:")
    print(f"   • Total Tests: {total_tests}")
    print(f"   • Successful: {successful_tests} ✅")
    print(f"   • Failed: {failed_tests} ❌")
    
    # Avoid division by zero
    if total_tests > 0:
        print(f"   • Success Rate: {(successful_tests/total_tests)*100:.1f}%")
        print(f"   • Average Time per Test: {total_duration/total_tests:.2f} seconds")
    else:
        print(f"   • Success Rate: N/A (no tests run)")
        print(f"   • Average Time per Test: N/A")
    
    print(f"   • Total Questions Processed: {total_questions}")
    print(f"   • Total Duration: {total_duration:.2f} seconds ({total_duration/60:.1f} minutes)")
    print(f"⏰ Test Completed: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    if failed_tests > 0:
        print(f"\n⚠  WARNING: {failed_tests} test(s) failed. Please check the logs above for details.")
    elif total_tests > 0:
        print(f"\n🎉 ALL TESTS PASSED! Your API is working perfectly.")
    else:
        print(f"\n⚠  WARNING: No tests were executed. Please check your test configuration.")
    
    print(f"{'='*80}\n")
    
    return test_results


if __name__ == "__main__":
    print("🚀 HackRX API Comprehensive Testing Suite")
    print("=" * 50)
    
    # Validate API URL before starting tests
    print(f"🔍 Checking API endpoint: {API_URL}")
    if not validate_api_url(API_URL):
        print(f"❌ WARNING: API endpoint may not be accessible!")
        response = input("Do you want to continue anyway? (y/N): ")
        if response.lower() not in ['y', 'yes']:
            print("🛑 Testing aborted.")
            sys.exit(1)
    else:
        print("✅ API endpoint is accessible!")
    
    # Option to run specific test cases
    print(f"\n📋 Available Test Options:")
    print("1. Run all tests (comprehensive)")
    print("2. Run insurance-related tests only")
    print("3. Run scientific document tests only")
    print("4. Run constitutional/legal document tests only")
    print("5. Run technical manual tests only")
    print("6. Run custom test (single payload)")
    
    choice = "1"  # Default choice
    test_type = "Comprehensive"  # Default test type
    
    try:
        choice = input("\nSelect test option (1-6) or press Enter for all tests: ").strip()
        if not choice:
            choice = "1"
        
        if choice == "1" or not choice:
            # Run all tests (default)
            test_payloads_to_run = test_payloads
            test_type = "Comprehensive"
        elif choice == "2":
            # Filter for insurance tests
            filtered_payloads = [p for p in test_payloads if any(keyword in p['documents'].lower() for keyword in ['policy', 'insurance', 'mediclaim', 'arogya', 'floater'])]
            test_payloads_to_run = filtered_payloads
            test_type = "Insurance_Documents"
        elif choice == "3":
            # Filter for scientific tests
            filtered_payloads = [p for p in test_payloads if 'principia' in p['documents'].lower()]
            test_payloads_to_run = filtered_payloads
            test_type = "Scientific_Documents"
        elif choice == "4":
            # Filter for constitutional tests
            filtered_payloads = [p for p in test_payloads if 'constitution' in p['documents'].lower()]
            test_payloads_to_run = filtered_payloads
            test_type = "Legal_Documents"
        elif choice == "5":
            # Filter for technical manual tests
            filtered_payloads = [p for p in test_payloads if 'splendor' in p['documents'].lower()]
            test_payloads_to_run = filtered_payloads
            test_type = "Technical_Manuals"
        elif choice == "6":
            # Custom single test
            print("\nAvailable documents:")
            for i, payload in enumerate(test_payloads, 1):
                doc_name = payload['documents'].split('/')[-1].split('?')[0]
                print(f"{i}. {doc_name} ({len(payload['questions'])} questions)")
            
            test_idx = int(input(f"\nSelect document (1-{len(test_payloads)}): ")) - 1
            test_payloads_to_run = [test_payloads[test_idx]]
            test_type = "Custom_Single_Test"
        else:
            # Run all tests (fallback)
            test_payloads_to_run = test_payloads
            test_type = "Comprehensive"
            
    except (ValueError, IndexError):
        print("Invalid selection. Running all tests...")
        test_payloads_to_run = test_payloads
        test_type = "Comprehensive"
    
    # Don't modify the global test_payloads, just pass the selected payloads to the function
    print(f"\n🎯 Selected Test Type: {test_type}")
    print(f"📊 Tests to run: {len(test_payloads_to_run)}")
    print(f"📝 Total questions: {sum(len(p['questions']) for p in test_payloads_to_run)}")
    
    # Run the tests with the selected payloads and capture results
    detailed_results = test_api_endpoint(test_payloads_to_run)
    
    # Generate timestamp for results file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_filename = f"hackrx_test_results_{timestamp}.json"
    
    # Add additional metadata to the results
    detailed_results["test_metadata"] = {
        "test_type": test_type,
        "selected_payloads_count": len(test_payloads_to_run),
        "total_available_payloads": len(test_payloads),
        "user_selection": choice,
        "api_url": API_URL
    }
    
    # Save detailed results
    save_test_results(detailed_results, results_filename)
    
    # Also create a summary-only file for quick overview
    summary_filename = f"hackrx_summary_{timestamp}.json"
    summary_results = {
        "test_summary": detailed_results["test_summary"],
        "test_metadata": detailed_results["test_metadata"],
        "test_cases_summary": [
            {
                "test_case_id": tc["test_case_id"],
                "document_type": tc["document_type"],
                "document_category": tc["document_category"],
                "status": tc["status"],
                "total_questions": tc["total_questions"],
                "processing_time": tc["processing_time"],
                "error_message": tc["error_message"] if tc["status"] == "failed" else None
            }
            for tc in detailed_results["test_cases"]
        ]
    }
    
    save_test_results(summary_results, summary_filename)
    
    print(f"\n📄 Results saved:")
    print(f"   • Detailed results: {results_filename}")
    print(f"   • Summary results: {summary_filename}")